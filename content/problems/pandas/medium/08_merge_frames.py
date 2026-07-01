# title: Merge Two Frames
# track: pandas
# difficulty: medium
# tags: pandas, merge
# description: |
# Merge two DataFrames on the 'id' column (inner join) and return the result.
# examples:
# merge_on_id(left, right) -> merged df
# hint: |
# pd.merge(left, right, on='id').
# syntax_hint: |
# pd.merge(left, right, on='id')


def merge_on_id(left, right) -> object:
    pass


def run_tests() -> None:
    import pandas as pd
    left = pd.DataFrame({'id': [1, 2], 'name': ['a', 'b']})
    right = pd.DataFrame({'id': [1, 2], 'score': [10, 20]})
    out = merge_on_id(left, right)
    assert list(out.columns) == ['id', 'name', 'score']
    assert len(out) == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
