# title: Squares of a Sorted Array
# track: algorithms
# difficulty: easy
# tags: two-pointers, array
# description: |
# Given a non-decreasing list that may have negatives, return the squares in non-decreasing order.
# examples:
# sorted_squares([-4,-1,0,3,10]) -> [0,1,9,16,100]
# hint: |
# Fill from the end using two pointers at both ends (largest absolute).
# syntax_hint: |
# result = [0]*n; for k in reversed(range(n)): ...


def sorted_squares(nums: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sorted_squares([0]) == [0]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
