import pandas as pd

def merge_on_id(left, right):
    return pd.merge(left, right, on='id')
