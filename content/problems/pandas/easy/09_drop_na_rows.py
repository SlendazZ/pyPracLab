# title: Drop NA Rows
# track: pandas
# difficulty: easy
# tags: pandas
# description: |
# Return a DataFrame with rows containing any NaN removed.
# examples:
# drop_na(df) removes rows with NaN
# hint: |
# df.dropna()
# syntax_hint: |
# df.dropna()


def drop_na(df):
    pass


def run_tests() -> None:
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({'a': [1, np.nan, 3]})
    out = drop_na(df)
    assert len(out) == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
