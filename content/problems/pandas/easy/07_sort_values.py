# title: Sort Values
# track: pandas
# difficulty: easy
# tags: pandas
# description: |
# Return the DataFrame sorted by the given column ascending.
# examples:
# sort_by(df, 'age') -> df sorted by age
# hint: |
# df.sort_values(column).
# syntax_hint: |
# df.sort_values(column).reset_index(drop=True)


def sort_by(df, column: str) -> object:
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'age': [30, 18, 21]})
    out = sort_by(df, 'age')
    assert list(out['age']) == [18, 21, 30]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
