def mean_salary(df):
    return df.groupby('dept')['salary'].mean().sort_index()
