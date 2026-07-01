# title: Two Sum (Unsorted)
# track: algorithms
# difficulty: easy
# tags: hash-map, array
# description: |
# Given an unsorted list and a target, return 0-based indexes of two numbers that add to target. Exactly one solution exists.
# examples:
# two_sum([2,7,11,15], 9) -> [0,1]
# hint: |
# Store value -> index as you scan; check if target - x was seen.
# syntax_hint: |
# seen = {}; for i, x in enumerate(nums): ...


def two_sum(nums: list[int], target: int) -> list[int]:
    pass


def run_tests() -> None:
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
