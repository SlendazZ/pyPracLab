# title: Move Zeroes
# track: algorithms
# difficulty: easy
# tags: two-pointers
# description: |
# Move all 0s to the end of the list in place, keeping the order of non-zero elements. Return the list.
# examples:
# move_zeroes([0,1,0,3,12]) -> [1,3,12,0,0]
# hint: |
# Keep a write index for the next non-zero; swap into place.
# syntax_hint: |
# for x in nums: if x != 0: nums[pos] = x; pos += 1


def move_zeroes(nums: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes([0]) == [0]
    assert move_zeroes([1]) == [1]
    assert move_zeroes([1, 0]) == [1, 0]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
