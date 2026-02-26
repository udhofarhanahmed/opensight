import pandas as pd
try:
    from rapidfuzz import process, fuzz
except ImportError:
    # Fallback if rapidfuzz is not installed
    process = None

def remove_duplicates(df: pd.DataFrame, key: str) -> pd.DataFrame:
    """
    Exact match deduplication.
    """
    return df.drop_duplicates(subset=[key], keep='first')

def fuzzy_deduplicate_customers(df: pd.DataFrame, threshold: int = 90) -> pd.DataFrame:
    """
    Fuzzy matching for customer names to catch near-duplicates.
    """
    if process is None or 'customer_name' not in df.columns:
        return df
    
    unique_names = df['customer_name'].unique()
    mapping = {}
    
    for name in unique_names:
        if name in mapping:
            continue
        
        # Find matches for this name
        matches = process.extract(name, unique_names, scorer=fuzz.token_sort_ratio, limit=10)
        for match_name, score, _ in matches:
            if score >= threshold:
                mapping[match_name] = name
                
    df['customer_name_clean'] = df['customer_name'].map(mapping)
    return df
