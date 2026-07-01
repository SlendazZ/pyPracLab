# title: Container With Most Water
# track: algorithms
# difficulty: medium
# tags: two-pointers
# description: |
# Each element is a wall height. Return the max water a pair of walls can hold (area = width * min height).
# examples:
# max_area([1,8,6,2,5,4,8,3,7]) -> 49
# hint: |
# Two pointers from the ends; move the shorter wall inward.
# syntax_hint: |
# while left < right: area = (right-left)*min(h[l], h[r])


def max_area(height: list[int]) -> int:
    pass


def run_tests() -> None:
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
