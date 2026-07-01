# title: Pivot Table Sum
# track: pandas
# difficulty: hard
# tags: pandas, pivot
# description: |
# Pivot df with index='dept', columns='month', values='sales', aggfunc='sum'.
# examples:
# pivot_sales(df) -> pivoted frame
# hint: |
# df.pivot_table(index='dept', columns='month', values='sales', aggfunc='sum')
# syntax_hint: |
# df.pivot_table(..., fill_value=0)


def pivot_sales(df):
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({
        'dept': ['a', 'a', 'b'],
        'month': ['jan', 'feb', 'jan'],
        'sales': [10, 20, 5],
    })
    out = pivot_sales(df)
    assert out.loc['a', 'jan'] == 10
    assert out.loc['b', 'jan'] == 5
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
