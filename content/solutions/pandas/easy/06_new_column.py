def with_total(df):
    df = df.copy()
    df['total'] = df['price'] * df['qty']
    return df
