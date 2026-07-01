# title: Word Counter App
# track: apps
# difficulty: easy
# tags: dict
# description: |
# Given a sentence, return a dict of lowercase word counts.
# examples:
# count_words("Hi hi there") -> {"hi":2,"there":1}
# hint: |
# Split on whitespace, lower, Counter.
# syntax_hint: |
# from collections import Counter


def count_words(sentence: str) -> dict[str, int]:
    pass


def run_tests() -> None:
    assert count_words("Hi hi there") == {"hi": 2, "there": 1}
    assert count_words("") == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
