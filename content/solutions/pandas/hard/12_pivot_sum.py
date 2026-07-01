def pivot_sales(df):
    return df.pivot_table(
        index='dept', columns='month', values='sales', aggfunc='sum', fill_value=0
    )
