# title: Counter - Top Words
# track: syntax
# difficulty: easy
# tags: collections
# description: |
# Return the n most common words (as (word, count) pairs) using collections.Counter.
# examples:
# top_words(["a","b","a","c","a","b"], 2) -> [("a",3),("b",2)]
# hint: |
# Counter(words).most_common(n) does exactly this.
# syntax_hint: |
# from collections import Counter; Counter(words).most_common(n)


def top_words(words: list[str], n: int) -> list[tuple[str, int]]:
    pass


def run_tests() -> None:
    assert top_words(["a", "b", "a", "c", "a", "b"], 2) == [("a", 3), ("b", 2)]
    assert top_words(["x"], 1) == [("x", 1)]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
