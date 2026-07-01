# title: Maximum Product Subarray
# track: algorithms
# difficulty: medium
# tags: dp, array
# description: |
# Given a list of integers, return the largest product of any contiguous non-empty subarray.
# examples:
# max_product([2,3,-2,4]) -> 6
# hint: |
# Track both max and min ending here because a negative flip can make a new max.
# syntax_hint: |
# cur_max = cur_min = best = nums[0]; update with x, cur_max*x, cur_min*x


def max_product(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-2]) == -2
    assert max_product([2, -5, -2, -4, 3]) == 24
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
