# title: Maximum Average Subarray I
# track: algorithms
# difficulty: easy
# tags: sliding-window
# description: |
# Return the max average of any contiguous subarray of length k.
# examples:
# max_avg([1,12,-5,-6,50,3], 4) -> 12.75
# hint: |
# Maintain a window sum of size k; slide and track the best.
# syntax_hint: |
# window = sum(nums[:k]); for i in range(k, len(nums)): window += nums[i] - nums[i-k]


def max_avg(nums: list[int], k: int) -> float:
    pass


def run_tests() -> None:
    assert max_avg([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert max_avg([5], 1) == 5.0
    assert abs(max_avg([0, 4, 0], 2) - 2.0) < 1e-9
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
