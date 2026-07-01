# title: Rolling Mean
# track: pandas
# difficulty: medium
# tags: pandas
# description: |
# Return a Series that is the rolling mean of values with the given window (min_periods=1).
# examples:
# rolling_mean(s, 2)
# hint: |
# s.rolling(window, min_periods=1).mean()
# syntax_hint: |
# s.rolling(window, min_periods=1).mean()


def rolling_mean(s, window: int):
    pass


def run_tests() -> None:
    import pandas as pd
    s = pd.Series([1, 2, 3, 4])
    out = rolling_mean(s, 2)
    assert abs(out.iloc[1] - 1.5) < 0.001
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
