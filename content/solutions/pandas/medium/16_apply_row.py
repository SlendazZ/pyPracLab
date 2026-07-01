def add_total(df):
    out = df.copy()
    out['total'] = out.apply(lambda r: r['a'] + r['b'], axis=1)
    return out
