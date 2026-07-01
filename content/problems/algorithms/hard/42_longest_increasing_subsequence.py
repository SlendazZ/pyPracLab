# title: Longest Increasing Subsequence Length
# track: algorithms
# difficulty: hard
# tags: dp, binary-search
# description: |
# Return the length of the longest strictly increasing subsequence.
# examples:
# lis_length([10,9,2,5,3,7,101,18]) -> 4
# hint: |
# Patience sorting: maintain a tails array; binary search insertion point.
# syntax_hint: |
# import bisect; bisect_left(tails, x)


def lis_length(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert lis_length([10,9,2,5,3,7,101,18]) == 4
    assert lis_length([0,1,0,3,2,3]) == 4
    assert lis_length([7,7,7,7]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
