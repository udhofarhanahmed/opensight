import pandas as pd

def remove_duplicates(df: pd.DataFrame, key: str) -> pd.DataFrame:
    """
    Simple exact match; could add fuzzy matching later
    """
    return df.drop_duplicates(subset=[key], keep='first')
