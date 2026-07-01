# title: Missing Number
# track: algorithms
# difficulty: easy
# tags: math, array
# description: |
# A list contains n distinct numbers taken from 0..n. Return the missing one.
# examples:
# missing([3,0,1]) -> 2
# missing([0,1]) -> 2
# hint: |
# The expected sum of 0..n is n*(n+1)/2; subtract the actual sum.
# syntax_hint: |
# n = len(nums); return n*(n+1)//2 - sum(nums)


def missing(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert missing([3, 0, 1]) == 2
    assert missing([0, 1]) == 2
    assert missing([0]) == 1
    assert missing([1, 0]) == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
