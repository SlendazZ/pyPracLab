# title: Insert Interval
# track: algorithms
# difficulty: medium
# tags: intervals
# description: |
# Insert new interval into sorted non-overlapping intervals; merge overlaps.
# examples:
# insert([[1,3],[6,9]], [2,5]) -> [[1,5],[6,9]]
# hint: |
# Add new; merge overlapping by expanding end.
# syntax_hint: |
# result = []; for interval: merge or append


def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    pass


def run_tests() -> None:
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([], [5,7]) == [[5,7]]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
