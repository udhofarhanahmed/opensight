from prefect import flow, task
import pandas as pd
from app.etl.processors import currency, deduplication
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
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply processors
    """
    if df.empty:
        return df
    
    # Currency normalization
    df = currency.normalise(df, target_currency='USD')
    
    # Deduplication
    if 'order_id' in df.columns:
        df = deduplication.remove_duplicates(df, key='order_id')
    
    # Basic date parsing
    if 'timestamp' in df.columns:
        df['timestamp_utc'] = pd.to_datetime(df['timestamp'])
    else:
        df['timestamp_utc'] = datetime.utcnow()
        
    return df

@task
def load_to_canonical(df: pd.DataFrame):
    """
    Insert into sales_event table
    """
    if df.empty:
        return
    
    db = SessionLocal()
    try:
        for _, row in df.iterrows():
            # Create SalesEvent
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
        cleaned_df = clean_data(raw_df)
        load_to_canonical(cleaned_df)
