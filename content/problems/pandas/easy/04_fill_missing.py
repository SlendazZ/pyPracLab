# title: Fill Missing Values
# track: pandas
# difficulty: easy
# tags: pandas
# description: |
# Given a Series with NaN values, return a Series where NaN is replaced by 0.
# examples:
# fill_zero(s) -> Series with no NaN
# hint: |
# s.fillna(0).
# syntax_hint: |
# s.fillna(0)


def fill_zero(s) -> object:
    pass


def run_tests() -> None:
    import pandas as pd
    import numpy as np
    s = pd.Series([1.0, np.nan, 3.0])
    out = fill_zero(s)
    assert list(out) == [1.0, 0.0, 3.0]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
