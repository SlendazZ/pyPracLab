# title: Search in Rotated Sorted Array
# track: algorithms
# difficulty: hard
# tags: binary-search, array
# description: |
# A sorted list was rotated at an unknown pivot. Given the rotated list and a target, return its index or -1 if absent. All values are distinct.
# examples:
# search_rotated([4,5,6,7,0,1,2], 0) -> 4
# hint: |
# Binary search; one half is always sorted — check which half contains target.
# syntax_hint: |
# mid = (lo + hi) // 2; if nums[lo] <= nums[mid]: left half sorted


def search_rotated(nums: list[int], target: int) -> int:
    pass


def run_tests() -> None:
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([1], 1) == 0
    assert search_rotated([3, 1], 1) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
