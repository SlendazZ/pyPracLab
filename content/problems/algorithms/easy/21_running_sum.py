# title: Running Sum
# track: algorithms
# difficulty: easy
# tags: prefix-sum, array
# description: |
# Return the running sum of a 1D list: output[i] is the sum of nums[0..i].
# examples:
# running_sum([1,2,3,4]) -> [1,3,6,10]
# hint: |
# Accumulate as you iterate.
# syntax_hint: |
# from itertools import accumulate; list(accumulate(nums))


def running_sum(nums: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1]) == [1, 2, 3]
    assert running_sum([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
