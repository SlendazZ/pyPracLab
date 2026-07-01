# title: Permutation in String
# track: algorithms
# difficulty: medium
# tags: sliding-window, string
# description: |
# Return True if s2 contains a substring that is a permutation of s1.
# examples:
# check_inclusion("ab", "eidbaooo") -> True
# hint: |
# Same fixed-window count technique as anagram finder.
# syntax_hint: |
# window size len(s1); compare Counter each step


def check_inclusion(s1: str, s2: str) -> bool:
    pass


def run_tests() -> None:
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("a", "a") is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
