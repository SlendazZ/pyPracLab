# title: Double a Series
# track: pandas
# difficulty: easy
# tags: pandas, series
# description: |
# Given a list of numbers, return a pandas Series with each value doubled.
# examples:
# list(double_series([1, 2, 3])) -> [2, 4, 6]
# hint: |
# pd.Series(values) * 2 vectorizes the doubling.
# syntax_hint: |
# import pandas as pd; return pd.Series(values) * 2


def double_series(values: list) -> object:
    pass


def run_tests() -> None:
    import pandas as pd
    s = double_series([1, 2, 3])
    assert isinstance(s, pd.Series)
    assert list(s) == [2, 4, 6]
    assert list(double_series([])) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
