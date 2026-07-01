def sort_by(df, column: str):
    return df.sort_values(column).reset_index(drop=True)
