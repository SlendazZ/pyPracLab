# title: Minimum Size Subarray Sum
# track: algorithms
# difficulty: medium
# tags: sliding-window
# description: |
# Return the minimal length of a contiguous subarray whose sum >= target, or 0.
# examples:
# min_subarray(7, [2,3,1,2,4,3]) -> 2
# hint: |
# Expand the right pointer; once the window hits the target, shrink from the left.
# syntax_hint: |
# while total >= target: best = min(best, right-left); total -= nums[left]


def min_subarray(target: int, nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert min_subarray(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray(4, [1, 4, 4]) == 1
    assert min_subarray(11, [1, 1, 1]) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
