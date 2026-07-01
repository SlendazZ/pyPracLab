# title: Pivot Table Mean
# track: pandas
# difficulty: medium
# tags: pandas, pivot
# description: |
# Pivot df with index='region', columns='product', values='sales', aggfunc='mean', fill_value=0.
# examples:
# pivot_mean(df) -> pivoted means
# hint: |
# df.pivot_table(index='region', columns='product', values='sales', aggfunc='mean')
# syntax_hint: |
# df.pivot_table(..., fill_value=0)


def pivot_mean(df):
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({
        'region': ['n', 'n', 's'],
        'product': ['a', 'a', 'b'],
        'sales': [10, 30, 5],
    })
    out = pivot_mean(df)
    assert out.loc['n', 'a'] == 20.0
    assert out.loc['s', 'b'] == 5.0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
