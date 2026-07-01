# title: Contains Duplicate
# track: algorithms
# difficulty: easy
# tags: set
# description: |
# Return True if any value appears at least twice in the list.
# examples:
# has_duplicate([1,2,3,1]) -> True
# has_duplicate([1,2,3]) -> False
# hint: |
# A set removes duplicates; compare lengths.
# syntax_hint: |
# return len(set(nums)) != len(nums)


def has_duplicate(nums: list[int]) -> bool:
    pass


def run_tests() -> None:
    assert has_duplicate([1, 2, 3, 1]) is True
    assert has_duplicate([1, 2, 3]) is False
    assert has_duplicate([]) is False
    assert has_duplicate([1]) is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
