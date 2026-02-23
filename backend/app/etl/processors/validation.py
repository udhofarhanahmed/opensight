import pandas as pd

def validate_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Simple data validation.
    Returns (valid_df, invalid_df)
    """
    if df.empty:
        return df, df
    
    # Required columns
    required_cols = ['order_id', 'amount', 'customer_id']
    
    # Check for missing required columns
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        # If critical columns are missing, all records are invalid
        df['error'] = f"Missing columns: {', '.join(missing_cols)}"
        return pd.DataFrame(columns=df.columns), df
    
    # Check for nulls in required columns
    is_valid = df[required_cols].notnull().all(axis=1)
    
    # Check for numeric amount
    is_valid &= pd.to_numeric(df['amount'], errors='coerce').notnull()
    
    valid_df = df[is_valid].copy()
    invalid_df = df[~is_valid].copy()
    
    if not invalid_df.empty:
        invalid_df['error'] = "Missing required data or invalid amount format"
        
    return valid_df, invalid_df
