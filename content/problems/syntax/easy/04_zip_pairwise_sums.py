# title: Zip - Pairwise Sums
# track: syntax
# difficulty: easy
# tags: zip
# description: |
# Given two equal-length lists, return a list of their element-wise sums using zip.
# examples:
# pairwise_sum([1,2,3],[10,20,30]) -> [11,22,33]
# hint: |
# zip(a, b) yields (a_i, b_i) pairs.
# syntax_hint: |
# [a + b for a, b in zip(xs, ys)]


def pairwise_sum(xs: list[int], ys: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert pairwise_sum([1, 2, 3], [10, 20, 30]) == [11, 22, 33]
    assert pairwise_sum([], []) == []
    assert pairwise_sum([1], [2]) == [3]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
