def astype_code(df):
    out = df.copy()
    out['code'] = out['code'].astype(str)
    return out
