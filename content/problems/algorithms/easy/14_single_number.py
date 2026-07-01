# title: Single Number
# track: algorithms
# difficulty: easy
# tags: bit-manipulation
# description: |
# Every element appears twice except one. Find that single one using O(1) space.
# examples:
# single([2,2,1]) -> 1
# single([4,1,2,1,2]) -> 4
# hint: |
# XOR cancels equal pairs: a ^ a == 0, and 0 ^ a == a.
# syntax_hint: |
# import functools, operator; functools.reduce(operator.xor, nums)


def single(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert single([2, 2, 1]) == 1
    assert single([4, 1, 2, 1, 2]) == 4
    assert single([1]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
