import pandas as pd

def normalise(df: pd.DataFrame, target_currency: str = 'USD') -> pd.DataFrame:
    """
    Normalise currency to a base currency.
    For now, assume simple conversion rates.
    """
    # Simple conversion map (could be replaced with an API call)
    rates = {
        'USD': 1.0,
        'PKR': 0.0036,
        'EUR': 1.08,
        'GBP': 1.26
    }
    
    def convert(row):
        currency = row.get('currency', 'USD')
        amount = row.get('amount', 0.0)
        rate = rates.get(currency, 1.0)
        return amount * rate
    
    df['net_amount'] = df.apply(convert, axis=1)
    return df
