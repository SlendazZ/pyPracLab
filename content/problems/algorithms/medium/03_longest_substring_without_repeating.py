# title: Longest Substring Without Repeating Characters
# track: algorithms
# difficulty: medium
# tags: sliding-window, hash-map
# description: |
# Given a string, return the length of the longest substring that contains no repeating characters.
# examples:
# length_of_longest("abcabcbb") -> 3
# length_of_longest("pwwkew") -> 3
# hint: |
# Slide a window with two pointers; store the last seen index of each character in a dict.
# syntax_hint: |
# for right, ch in enumerate(s): move left to max(left, last[ch] + 1)


def length_of_longest(s: str) -> int:
    pass


def run_tests() -> None:
    assert length_of_longest("abcabcbb") == 3
    assert length_of_longest("bbbbb") == 1
    assert length_of_longest("pwwkew") == 3
    assert length_of_longest("") == 0
    assert length_of_longest("abcdef") == 6
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
