# title: Filter a DataFrame
# track: pandas
# difficulty: easy
# tags: pandas, dataframe
# description: |
# Given a DataFrame with an 'age' column, return rows where age >= 18.
# examples:
# adults(df) -> df with only age >= 18
# hint: |
# Boolean indexing: df[df['age'] >= 18].
# syntax_hint: |
# df[df['age'] >= 18]


def adults(df) -> object:
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'name': ['a', 'b', 'c'], 'age': [10, 18, 21]})
    out = adults(df)
    assert list(out['name']) == ['b', 'c']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
