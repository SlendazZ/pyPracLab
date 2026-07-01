def melt_wide(df):
    return df.melt(id_vars=['id'], value_vars=['a', 'b'])
