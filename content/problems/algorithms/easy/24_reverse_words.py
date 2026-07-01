# title: Reverse Words in a String III
# track: algorithms
# difficulty: easy
# tags: string
# description: |
# Reverse the order of characters in each word of s, keeping word order and single spaces.
# examples:
# reverse_words("Let us take contest") -> "teL su ekat tsetnoc"
# hint: |
# Split, reverse each word, join.
# syntax_hint: |
# ' '.join(w[::-1] for w in s.split())


def reverse_words(s: str) -> str:
    pass


def run_tests() -> None:
    assert reverse_words("Let us go") == "teL su og"
    assert reverse_words("hello") == "olleh"
    assert reverse_words("a b c") == "a b c"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
