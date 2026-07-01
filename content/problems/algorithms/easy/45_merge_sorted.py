# title: Merge Two Sorted Lists
# track: algorithms
# difficulty: easy
# tags: two-pointers, array
# description: |
# Given two sorted lists of integers, return a new sorted list containing all elements from both.
# examples:
# merge_sorted([1,3,5], [2,4,6]) -> [1,2,3,4,5,6]
# hint: |
# Compare the fronts of both lists with two pointers; append the smaller value each step.
# syntax_hint: |
# while i < len(a) and j < len(b): pick a[i] or b[j]


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1, 2]) == [1, 2]
    assert merge_sorted([1], []) == [1]
    assert merge_sorted([], []) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
