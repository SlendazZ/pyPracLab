def unique_cities(df) -> int:
    if df.empty or 'city' not in df.columns:
        return 0
    return int(df['city'].nunique())
