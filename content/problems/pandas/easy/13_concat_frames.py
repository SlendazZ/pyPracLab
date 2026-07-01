# title: Concat DataFrames
# track: pandas
# difficulty: easy
# tags: pandas, concat
# description: |
# Vertically concatenate a list of DataFrames with ignore_index=True.
# examples:
# concat_frames([df1, df2]) -> combined frame
# hint: |
# pd.concat(frames, ignore_index=True)
# syntax_hint: |
# import pandas as pd; pd.concat(frames, ignore_index=True)


def concat_frames(frames: list):
    pass


def run_tests() -> None:
    import pandas as pd
    a = pd.DataFrame({'x': [1]})
    b = pd.DataFrame({'x': [2, 3]})
    out = concat_frames([a, b])
    assert list(out['x']) == [1, 2, 3]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
