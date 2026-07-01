# title: Longest Repeating Character Replacement
# track: algorithms
# difficulty: medium
# tags: sliding-window, string
# description: |
# Given string s and int k, return length of longest substring containing same letter after at most k replacements.
# examples:
# character_replacement("ABAB", 2) -> 4
# hint: |
# Expand window; track max char frequency; shrink when window - max_freq > k.
# syntax_hint: |
# max_freq = max(counts.values()); while right-left+1-max_freq > k: shrink


def character_replacement(s: str, k: int) -> int:
    pass


def run_tests() -> None:
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
