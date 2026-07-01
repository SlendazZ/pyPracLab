# title: Length of Last Word
# track: algorithms
# difficulty: easy
# tags: string
# description: |
# Return the length of the last word in s (words separated by spaces, possibly trailing spaces).
# examples:
# last_word_len("Hello World") -> 5
# last_word_len("   fly me   to   the moon  ") -> 4
# hint: |
# Strip trailing spaces, split, take the last word's length.
# syntax_hint: |
# return len(s.rstrip().split()[-1])


def last_word_len(s: str) -> int:
    pass


def run_tests() -> None:
    assert last_word_len("Hello World") == 5
    assert last_word_len("   fly me   to   the moon  ") == 4
    assert last_word_len("a") == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
