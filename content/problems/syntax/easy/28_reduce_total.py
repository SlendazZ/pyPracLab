# title: Reduce to Total
# track: syntax
# difficulty: easy
# tags: functools
# description: |
# Return the sum of a list of integers using functools.reduce.
# examples:
# total([1,2,3]) -> 6
# hint: |
# functools.reduce(operator.add, nums, 0)
# syntax_hint: |
# from functools import reduce; import operator


def total(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert total([1, 2, 3]) == 6
    assert total([]) == 0
    assert total([5]) == 5
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
