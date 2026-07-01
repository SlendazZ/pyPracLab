# title: Sort Colors
# track: algorithms
# difficulty: medium
# tags: array, two-pointers
# description: |
# Sort a list of 0s, 1s, and 2s in-place style — return a new sorted list.
# examples:
# sort_colors([2,0,2,1,1,0]) -> [0,0,1,1,2,2]
# hint: |
# Dutch national flag with three pointers low, mid, high.
# syntax_hint: |
# while mid <= high: swap 0 to front, 2 to back


def sort_colors(nums: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert sort_colors([2, 0, 1]) == [0, 1, 2]
    assert sort_colors([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
