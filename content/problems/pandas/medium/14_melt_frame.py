# title: Melt DataFrame
# track: pandas
# difficulty: medium
# tags: pandas, reshape
# description: |
# Melt df with id_vars=['id'] and value_vars=['a','b']; return long-format frame.
# examples:
# melt_wide(df) unpivots a and b columns
# hint: |
# df.melt(id_vars=['id'], value_vars=['a','b'])
# syntax_hint: |
# df.melt(id_vars=['id'], value_vars=['a', 'b'], var_name='key', value_name='val')


def melt_wide(df):
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'id': [1], 'a': [10], 'b': [20]})
    out = melt_wide(df)
    assert len(out) == 2
    assert set(out['variable']) == {'a', 'b'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
