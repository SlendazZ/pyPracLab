# title: Coin Change
# track: algorithms
# difficulty: medium
# tags: dp
# description: |
# Given coin denominations and an amount, return the fewest coins to make the amount, or -1.
# examples:
# coins([1,2,5], 11) -> 3
# coins([2], 3) -> -1
# hint: |
# Bottom-up DP: dp[a] = min(dp[a-coin] + 1) for each coin.
# syntax_hint: |
# dp = [inf]*(amount+1); dp[0] = 0; for a in range(1, amount+1): ...


def coins(coins: list[int], amount: int) -> int:
    pass


def run_tests() -> None:
    assert coins([1, 2, 5], 11) == 3
    assert coins([2], 3) == -1
    assert coins([1], 0) == 0
    assert coins([1], 2) == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
