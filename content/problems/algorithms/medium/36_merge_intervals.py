# title: Merge Intervals
# track: algorithms
# difficulty: medium
# tags: intervals, sort
# description: |
# Given a list of [start, end] intervals, merge all overlapping ones and return the merged list.
# examples:
# merge([[1,3],[2,6],[8,10]]) -> [[1,6],[8,10]]
# hint: |
# Sort by start; extend the current interval when they overlap.
# syntax_hint: |
# for start, end in sorted(intervals): if start <= cur_end: cur_end = max(...)


def merge(intervals: list[list[int]]) -> list[list[int]]:
    pass


def run_tests() -> None:
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 2]]) == [[1, 2]]
    assert merge([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
