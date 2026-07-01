# title: Nunique Column
# track: pandas
# difficulty: easy
# tags: pandas, aggregate
# description: |
# Return the number of unique values in column 'city'.
# examples:
# unique_cities(df) -> int count
# hint: |
# df['city'].nunique()
# syntax_hint: |
# df['city'].nunique()


def unique_cities(df) -> int:
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'city': ['a', 'b', 'a', 'c']})
    assert unique_cities(df) == 3
    assert unique_cities(pd.DataFrame({'city': []})) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
