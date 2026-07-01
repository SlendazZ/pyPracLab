# title: Edit Distance
# track: algorithms
# difficulty: hard
# tags: dp, string
# description: |
# Return the minimum number of single-character edits (insert, delete, replace) to turn word1 into word2.
# examples:
# edit_distance("horse", "ros") -> 3
# hint: |
# Classic 2D DP: dp[i][j] from prefixes of word1 and word2.
# syntax_hint: |
# if w1[i-1]==w2[j-1]: dp[i][j]=dp[i-1][j-1] else min of three neighbors +1


def edit_distance(word1: str, word2: str) -> int:
    pass


def run_tests() -> None:
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("", "a") == 1
    assert edit_distance("abc", "abc") == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
