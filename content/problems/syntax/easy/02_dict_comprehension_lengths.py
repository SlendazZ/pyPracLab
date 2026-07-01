# title: Dict Comprehension - Lengths
# track: syntax
# difficulty: easy
# tags: comprehension, dict
# description: |
# Return a dict mapping each word to its length, using a dict comprehension.
# examples:
# lengths(["hi","there"]) -> {"hi":2,"there":5}
# hint: |
# {word: len(word) for word in words}
# syntax_hint: |
# dict comprehension has the form {key: value for ...}.


def lengths(words: list[str]) -> dict[str, int]:
    pass


def run_tests() -> None:
    assert lengths(["hi", "there"]) == {"hi": 2, "there": 5}
    assert lengths([]) == {}
    assert lengths(["x"]) == {"x": 1}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
