# title: GroupBy Mean
# track: pandas
# difficulty: medium
# tags: pandas, groupby
# description: |
# Given a DataFrame with 'dept' and 'salary', return a Series of mean salary per dept (sorted by dept name).
# examples:
# mean_salary(df) -> Series indexed by dept
# hint: |
# df.groupby('dept')['salary'].mean().sort_index().
# syntax_hint: |
# df.groupby('dept')['salary'].mean().sort_index()


def mean_salary(df) -> object:
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'dept': ['a', 'a', 'b'], 'salary': [10, 20, 30]})
    out = mean_salary(df)
    assert out['a'] == 15.0
    assert out['b'] == 30.0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
