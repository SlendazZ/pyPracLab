# title: Between Filter
# track: pandas
# difficulty: easy
# tags: pandas, filter
# description: |
# Return rows where column 'score' is between low and high inclusive.
# examples:
# between_scores(df, 10, 20) filters score column
# hint: |
# df[df['score'].between(low, high)]
# syntax_hint: |
# df['score'].between(low, high)


def between_scores(df, low: int, high: int):
    pass


def run_tests() -> None:
    import pandas as pd
    df = pd.DataFrame({'score': [5, 15, 25]})
    out = between_scores(df, 10, 20)
    assert list(out['score']) == [15]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
