# title: Valid Anagram
# track: algorithms
# difficulty: easy
# tags: hash-map, string
# description: |
# Return True if string t is an anagram of string s (same characters, same counts).
# examples:
# is_anagram("anagram","nagaram") -> True
# is_anagram("rat","car") -> False
# hint: |
# collections.Counter compares counts directly.
# syntax_hint: |
# from collections import Counter; return Counter(s) == Counter(t)


def is_anagram(s: str, t: str) -> bool:
    pass


def run_tests() -> None:
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "a") is True
    assert is_anagram("ab", "ba") is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
