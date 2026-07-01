# title: Find Pivot Index
# track: algorithms
# difficulty: easy
# tags: prefix-sum
# description: |
# The pivot index is where the sum of elements to the left equals the sum to the right. Return it, or -1.
# examples:
# pivot([1,7,3,6,5,6]) -> 3
# pivot([1,2,3]) -> -1
# hint: |
# Total sum minus left_sum minus nums[i] gives the right sum.
# syntax_hint: |
# for i, x in enumerate(nums): if left == total - left - x: return i


def pivot(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert pivot([1, 7, 3, 6, 5, 6]) == 3
    assert pivot([1, 2, 3]) == -1
    assert pivot([2, 1, -1]) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
