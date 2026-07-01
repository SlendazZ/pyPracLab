# title: Remove Duplicates from Sorted Array
# track: algorithms
# difficulty: easy
# tags: two-pointers
# description: |
# Remove duplicates in place from a sorted list and return the count of unique elements (the first k slots hold them).
# examples:
# remove_dups([1,1,2]) -> 2  (list becomes [1,2,_])
# hint: |
# Keep a write index; advance it only when a new value appears.
# syntax_hint: |
# for x in nums: if write == 0 or x != nums[write-1]: nums[write] = x; write += 1


def remove_dups(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    a = [1, 1, 2]
    k = remove_dups(a)
    assert k == 2 and a[:k] == [1, 2]
    b = [0, 0, 1, 1, 2, 2, 3]
    k = remove_dups(b)
    assert k == 4 and b[:k] == [0, 1, 2, 3]
    assert remove_dups([1]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
