# title: Value Counts
# track: pandas
# difficulty: easy
# tags: pandas
# description: |
# Return the counts of each unique value in a Series, sorted by count descending.
# examples:
# counts(pd.Series([1,1,2])) -> {1:2, 2:1}
# hint: |
# s.value_counts() returns a Series sorted descending.
# syntax_hint: |
# s.value_counts().to_dict()


def counts(s) -> dict:
    pass


def run_tests() -> None:
    import pandas as pd
    out = counts(pd.Series([1, 1, 2]))
    assert out == {1: 2, 2: 1}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
