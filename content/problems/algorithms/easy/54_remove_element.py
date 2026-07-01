# title: Remove Element
# track: algorithms
# difficulty: easy
# tags: array, two-pointers
# description: |
# Return a new list with all occurrences of val removed, preserving order of remaining elements.
# examples:
# remove_val([3,2,2,3], 3) -> [2,2]
# hint: |
# Scan and keep elements not equal to val.
# syntax_hint: |
# return [x for x in nums if x != val]


def remove_val(nums: list[int], val: int) -> list[int]:
    pass


def run_tests() -> None:
    assert remove_val([3, 2, 2, 3], 3) == [2, 2]
    assert remove_val([0, 1, 2, 2, 3, 0, 4, 2], 2) == [0, 1, 3, 0, 4]
    assert remove_val([], 1) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
