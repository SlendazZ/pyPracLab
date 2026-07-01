# title: Apply Row Function
# track: pandas
# difficulty: medium
# tags: pandas, apply
# description: |
# Add column 'total' as sum of columns 'a' and 'b' using apply along rows.
# examples:
# add_total(df) -> df with total column
# hint: |
# df.apply(lambda row: row['a'] + row['b'], axis=1)
# syntax_hint: |
# df['total'] = df.apply(lambda r: r['a'] + r['b'], axis=1)


def add_total(df):
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    out = add_total(df)
    assert list(out['total']) == [4, 6]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
