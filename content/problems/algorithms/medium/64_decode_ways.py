# title: Decode Ways
# track: algorithms
# difficulty: medium
# tags: dp, string
# description: |
# A=1..Z=26 mapping; count how many ways to decode digit string.
# examples:
# num_decodings("12") -> 2
# hint: |
# dp[i] += dp[i-1] if valid single; += dp[i-2] if valid pair.
# syntax_hint: |
# if s[i-1] != '0': dp[i] += dp[i-1]


def num_decodings(s: str) -> int:
    pass


def run_tests() -> None:
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
