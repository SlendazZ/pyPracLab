# title: Top K Frequent Elements
# track: algorithms
# difficulty: medium
# tags: hash-map, heap
# description: |
# Return the k most frequent elements from nums (any order).
# examples:
# top_k([1,1,1,2,2,3], 2) -> [1,2]
# hint: |
# Counter, then take the k largest by frequency.
# syntax_hint: |
# from collections import Counter; Counter(nums).most_common(k)


def top_k(nums: list[int], k: int) -> list[int]:
    pass


def run_tests() -> None:
    assert sorted(top_k([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k([1], 1) == [1]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
