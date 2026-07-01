# title: Astype Column
# track: pandas
# difficulty: easy
# tags: pandas, types
# description: |
# Convert column 'code' to string dtype and return the DataFrame.
# examples:
# astype_code(df) -> code column is str
# hint: |
# df.assign(code=df['code'].astype(str)) or df.copy with astype
# syntax_hint: |
# df['code'] = df['code'].astype(str)


def astype_code(df):
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'code': [1, 2]})
    out = astype_code(df)
    assert out['code'].iloc[0] == '1'
    assert out['code'].iloc[1] == '2'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
