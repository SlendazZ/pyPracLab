# title: Unique Paths
# track: algorithms
# difficulty: medium
# tags: dp, grid
# description: |
# Robot at top-left of m x n grid; only move right/down. Return number of paths to bottom-right.
# examples:
# unique_paths(3, 7) -> 28
# hint: |
# dp[r][c] = dp[r-1][c] + dp[r][c-1]; first row/col are 1.
# syntax_hint: |
# dp = [[1]*n for _ in range(m)]


def unique_paths(m: int, n: int) -> int:
    pass


def run_tests() -> None:
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 1) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
