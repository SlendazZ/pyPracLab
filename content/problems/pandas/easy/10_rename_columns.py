# title: Rename Columns
# track: pandas
# difficulty: easy
# tags: pandas
# description: |
# Rename DataFrame columns using the given mapping dict.
# examples:
# rename_cols(df, {'old':'new'})
# hint: |
# df.rename(columns=mapping)
# syntax_hint: |
# df.rename(columns=mapping)


def rename_cols(df, mapping: dict):
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'old': [1]})
    out = rename_cols(df, {'old': 'new'})
    assert 'new' in out.columns
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
