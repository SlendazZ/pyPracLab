# title: Two Sum II - Input Array Is Sorted
# track: algorithms
# difficulty: easy
# tags: two-pointers, array
# description: |
# Given a sorted list of numbers and a target, return the 1-based indexes of the two numbers that add up to target. Exactly one answer exists.
# examples:
# two_sum_sorted([2, 7, 11, 15], 9) -> [1, 2]
# hint: |
# The list is sorted, so use two pointers: one at the start, one at the end.
# syntax_hint: |
# while left < right: ... ; list indexes are 0-based, so return +1.


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    pass


def run_tests() -> None:
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
    assert two_sum_sorted([1, 2, 3, 4, 6], 10) == [4, 5]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
