# title: Maximum Subarray
# track: algorithms
# difficulty: medium
# tags: dp, array
# description: |
# Find the contiguous subarray with the largest sum and return the sum.
# examples:
# max_subarray([-2,1,-3,4,-1,2,1,-5,4]) -> 6
# hint: |
# Kadane's algorithm: keep a running sum; reset to 0 when it goes negative.
# syntax_hint: |
# for x in nums: cur = max(x, cur + x); best = max(best, cur)


def max_subarray(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-1]) == -1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
