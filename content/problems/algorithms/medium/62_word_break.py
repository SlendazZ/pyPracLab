# title: Word Break
# track: algorithms
# difficulty: medium
# tags: dp, string
# description: |
# Return True if s can be segmented into space-separated words from the dictionary.
# examples:
# word_break("leetcode", ["leet","code"]) -> True
# hint: |
# dp[i] = any dp[j] and s[j:i] in word_set for j < i.
# syntax_hint: |
# dp = [False]*(n+1); dp[0]=True


def word_break(s: str, word_dict: list[str]) -> bool:
    pass


def run_tests() -> None:
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats","dog","sand","and","cat"]) is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
