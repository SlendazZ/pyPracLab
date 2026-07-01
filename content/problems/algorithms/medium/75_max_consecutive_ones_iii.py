# title: Max Consecutive Ones III
# track: algorithms
# difficulty: medium
# tags: sliding-window, array
# description: |
# Binary array and k flips allowed; return max length of subarray of all 1s after at most k flips.
# examples:
# longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) -> 6
# hint: |
# Sliding window; shrink when zeros in window > k.
# syntax_hint: |
# while zeros > k: shrink left


def longest_ones(nums: list[int], k: int) -> int:
    pass


def run_tests() -> None:
    assert longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
    assert longest_ones([1], 0) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
