# title: Kth Largest Element
# track: algorithms
# difficulty: medium
# tags: heap, array
# description: |
# Given an unsorted list and integer k, return the kth largest element (1-based: k=1 is the maximum).
# examples:
# kth_largest([3,2,1,5,6,4], 2) -> 5
# hint: |
# Use heapq.nlargest(k, nums)[-1] or maintain a size-k min-heap.
# syntax_hint: |
# import heapq; return heapq.nlargest(k, nums)[-1]


def kth_largest(nums: list[int], k: int) -> int:
    pass


def run_tests() -> None:
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([1], 1) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
