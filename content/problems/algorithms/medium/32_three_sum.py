# title: 3Sum
# track: algorithms
# difficulty: medium
# tags: two-pointers, array
# description: |
# Return all unique triplets [a,b,c] from nums that sum to 0 (no duplicate triplets).
# examples:
# three_sum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]
# hint: |
# Sort; for each index, two-pointer the rest; skip duplicates.
# syntax_hint: |
# nums.sort(); for i,a in enumerate(nums): if i>0 and a==nums[i-1]: continue


def three_sum(nums: list[int]) -> list[list[int]]:
    pass


def run_tests() -> None:
    r = three_sum([-1, 0, 1, 2, -1, -4])
    r = sorted([sorted(t) for t in r])
    assert r == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([]) == []
    assert three_sum([0]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
