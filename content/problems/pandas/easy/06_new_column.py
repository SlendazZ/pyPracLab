# title: Add a Computed Column
# track: pandas
# difficulty: easy
# tags: pandas, dataframe
# description: |
# Given a DataFrame with 'price' and 'qty', return it with a new 'total' column = price * qty.
# examples:
# with_total(df) -> df with 'total'
# hint: |
# df.assign(total=df['price']*df['qty']) or df['total']=....
# syntax_hint: |
# df['total'] = df['price'] * df['qty']; return df


def with_total(df) -> object:
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'price': [2, 3], 'qty': [4, 5]})
    out = with_total(df.copy())
    assert list(out['total']) == [8, 15]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
