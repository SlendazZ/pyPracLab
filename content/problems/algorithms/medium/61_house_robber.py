# title: House Robber
# track: algorithms
# difficulty: medium
# tags: dp, array
# description: |
# Rob non-adjacent houses for max money; return maximum loot.
# examples:
# rob([2,7,9,3,1]) -> 12
# hint: |
# DP: at each house take max(skip, take+prev_skip).
# syntax_hint: |
# prev2, prev1 = 0, 0; for x: prev2, prev1 = prev1, max(prev1, prev2+x)


def rob(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([1, 2, 3, 1]) == 4
    assert rob([0]) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
