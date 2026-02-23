from prefect import flow, task
import pandas as pd
from app.etl.processors import currency, deduplication, validation
from app.models.base import SessionLocal
from app.models.raw import RawEvent
from app.models.sales_event import SalesEvent
from datetime import datetime

@task
def extract_raw_events():
    """
    Load from raw_events table (unprocessed)
    """
    db = SessionLocal()
    try:
        raw_events = db.query(RawEvent).filter(RawEvent.status == "pending").all()
        if not raw_events:
            return pd.DataFrame()
        
        # Flatten the data from JSONB
        data = [event.data for event in raw_events]
        df = pd.DataFrame(data)
        # Add raw_event_id to track back
        df['raw_event_id'] = [event.id for event in raw_events]
        return df
    finally:
        db.close()

@task
def clean_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Apply processors and validation.
    Returns (valid_df, invalid_df)
    """
    if df.empty:
        return df, df
    
    # 1. Validation
    valid_df, invalid_df = validation.validate_data(df)
    if valid_df.empty:
        return valid_df, invalid_df
    
    # 2. Currency normalization
    valid_df = currency.normalise(valid_df, target_currency='USD')
    
    # 3. Deduplication
    if 'order_id' in valid_df.columns:
        valid_df = deduplication.remove_duplicates(valid_df, key='order_id')
    
    # 4. Fuzzy deduplication for customers (optional)
    if 'customer_name' in valid_df.columns:
        valid_df = deduplication.fuzzy_deduplicate_customers(valid_df)
    
    # 5. Basic date parsing
    if 'timestamp' in valid_df.columns:
        valid_df['timestamp_utc'] = pd.to_datetime(valid_df['timestamp'])
    else:
        valid_df['timestamp_utc'] = datetime.utcnow()
        
    return valid_df, invalid_df

@task
def load_to_canonical(valid_df: pd.DataFrame, invalid_df: pd.DataFrame):
    """
    Insert into sales_event table and handle invalid records.
    """
    db = SessionLocal()
    try:
        # Load valid records
        if not valid_df.empty:
            for _, row in valid_df.iterrows():
                sales_event = SalesEvent(
                    order_id=str(row.get('order_id')),
                    customer_id=str(row.get('customer_id')),
                    product_id=str(row.get('product_id')),
                    amount=float(row.get('amount', 0.0)),
                    currency=str(row.get('currency', 'USD')),
                    net_amount=float(row.get('net_amount', 0.0)),
                    channel=str(row.get('channel', 'Unknown')),
                    status=str(row.get('status', 'completed')),
                    timestamp_utc=row.get('timestamp_utc'),
                    raw_event_id=int(row.get('raw_event_id'))
                )
                db.add(sales_event)
                
                # Update RawEvent status
                raw_event = db.query(RawEvent).filter(RawEvent.id == int(row.get('raw_event_id'))).first()
                if raw_event:
                    raw_event.status = "processed"
        
        # Handle invalid records
        if not invalid_df.empty:
            for _, row in invalid_df.iterrows():
                raw_event = db.query(RawEvent).filter(RawEvent.id == int(row.get('raw_event_id'))).first()
                if raw_event:
                    raw_event.status = "failed"
                    # Could store error message in a separate table or JSON field
        
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error loading data: {e}")
    finally:
        db.close()

@flow
def etl_pipeline():
    raw_df = extract_raw_events()
    if not raw_df.empty:
        valid_df, invalid_df = clean_data(raw_df)
        load_to_canonical(valid_df, invalid_df)
