# title: Find Duplicate Number
# track: algorithms
# difficulty: easy
# tags: array, two-pointers
# description: |
# Array of n+1 integers in range 1..n with exactly one duplicate. Return the duplicate.
# examples:
# find_duplicate([1,3,4,2,2]) -> 2
# hint: |
# Treat as linked list cycle (Floyd); or binary search on value range.
# syntax_hint: |
# slow=fast=nums[0]; cycle detection


def find_duplicate(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    assert find_duplicate([3, 1, 3, 4, 2]) == 3
    assert find_duplicate([1, 1]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
