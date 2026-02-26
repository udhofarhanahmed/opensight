import pandas as pd
import requests
from functools import lru_cache

@lru_cache(maxsize=1)
def get_live_rates():
    """
    Fetch live exchange rates from a free API.
    """
    try:
        # Using a free API (exchangerate-api.com)
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        if response.status_code == 200:
            return response.json().get('rates', {})
    except Exception as e:
        print(f"Error fetching live rates: {e}")
    
    # Fallback rates
    return {
        'USD': 1.0,
        'PKR': 0.0036,
        'EUR': 1.08,
        'GBP': 1.26
    }

def normalise(df: pd.DataFrame, target_currency: str = 'USD') -> pd.DataFrame:
    """
    Normalise currency to a base currency.
    """
    rates = get_live_rates()
    
    def convert(row):
        currency = row.get('currency', 'USD')
        amount = row.get('amount', 0.0)
        rate = rates.get(currency, 1.0)
        return amount * rate
    
    df['net_amount'] = df.apply(convert, axis=1)
    return df
