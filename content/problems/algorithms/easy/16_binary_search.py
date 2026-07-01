# title: Binary Search
# track: algorithms
# difficulty: easy
# tags: binary-search
# description: |
# Return the index of target in a sorted list, or -1 if absent.
# examples:
# bsearch([-1,0,3,5,9,12], 9) -> 4
# bsearch([-1,0,3,5,9,12], 2) -> -1
# hint: |
# Narrow the [lo, hi] window by comparing the midpoint to the target.
# syntax_hint: |
# while lo <= hi: mid = (lo + hi) // 2


def bsearch(nums: list[int], target: int) -> int:
    pass


def run_tests() -> None:
    assert bsearch([-1, 0, 3, 5, 9, 12], 9) == 4
    assert bsearch([-1, 0, 3, 5, 9, 12], 2) == -1
    assert bsearch([1], 1) == 0
    assert bsearch([1], 0) == -1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
