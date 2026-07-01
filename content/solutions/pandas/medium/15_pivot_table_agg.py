def pivot_mean(df):
    return df.pivot_table(
        index='region', columns='product', values='sales', aggfunc='mean', fill_value=0
    )
