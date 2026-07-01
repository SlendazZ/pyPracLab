# title: Subarray Sum Equals K
# track: algorithms
# difficulty: medium
# tags: hash-map, prefix-sum
# description: |
# Given a list of integers (may include negatives) and an integer k, return the number of contiguous subarrays whose sum equals k.
# examples:
# subarray_sum_k([1,1,1], 2) -> 2
# hint: |
# Track prefix sums in a dict; for each prefix p, add count of prefixes equal to p - k.
# syntax_hint: |
# counts = {0: 1}; running = 0; running += x; ans += counts.get(running - k, 0)


def subarray_sum_k(nums: list[int], k: int) -> int:
    pass


def run_tests() -> None:
    assert subarray_sum_k([1, 1, 1], 2) == 2
    assert subarray_sum_k([1, 2, 3], 3) == 2
    assert subarray_sum_k([1, -1, 0], 0) == 3
    assert subarray_sum_k([], 0) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
