# title: Word Frequency
# track: automations
# difficulty: easy
# tags: collections, string
# description: |
# Given a string of whitespace-separated words, return a dict mapping each lowercase word to its count.
# examples:
# word_counts("a b a") -> {"a":2,"b":1}
# hint: |
# collections.Counter counts an iterable of words.
# syntax_hint: |
# text.lower().split() lowercases and splits on any whitespace.


def word_counts(text: str) -> dict[str, int]:
    pass


def run_tests() -> None:
    assert word_counts("a b a") == {"a": 2, "b": 1}
    assert word_counts("Hello hello") == {"hello": 2}
    assert word_counts("") == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
