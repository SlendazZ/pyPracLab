# title: Trapping Rain Water
# track: algorithms
# difficulty: hard
# tags: two-pointers, array
# description: |
# Given non-negative elevation bars, return how much water can be trapped after raining.
# examples:
# trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6
# hint: |
# Two pointers from both ends; track left_max and right_max.
# syntax_hint: |
# while left < right: move the side with smaller max.


def trap(height: list[int]) -> int:
    pass


def run_tests() -> None:
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([]) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
