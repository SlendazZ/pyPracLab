# title: Find All Anagrams
# track: algorithms
# difficulty: medium
# tags: sliding-window, string
# description: |
# Given strings s and p, return sorted list of start indices in s where an anagram of p begins.
# examples:
# find_anagrams("cbaebabacd", "abc") -> [0, 6]
# hint: |
# Fixed window of len(p); compare character counts.
# syntax_hint: |
# from collections import Counter; need = Counter(p)


def find_anagrams(s: str, p: str) -> list[int]:
    pass


def run_tests() -> None:
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]
    assert find_anagrams("aaaa", "aa") == [0, 1, 2]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
