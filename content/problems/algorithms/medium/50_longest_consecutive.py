# title: Longest Consecutive Sequence
# track: algorithms
# difficulty: medium
# tags: hash-set, array
# description: |
# Given an unsorted list of integers, return the length of the longest consecutive elements sequence. Must run in O(n) time.
# examples:
# longest_consecutive([100,4,200,1,3,2]) -> 4  # sequence 1,2,3,4
# hint: |
# Put all numbers in a set; only start counting from numbers with no predecessor (n-1 not in set).
# syntax_hint: |
# nums_set = set(nums); if (x - 1) not in nums_set: walk x, x+1, ...


def longest_consecutive(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
