def between_scores(df, low: int, high: int):
    return df[df['score'].between(low, high)]
