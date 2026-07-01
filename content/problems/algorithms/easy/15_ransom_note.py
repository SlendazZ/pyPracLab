# title: Ransom Note
# track: algorithms
# difficulty: easy
# tags: hash-map, string
# description: |
# Return True if the ransom note can be constructed from the magazine's letters (each letter used once).
# examples:
# can_build("aa","ab") -> False
# can_build("aa","aab") -> True
# hint: |
# Count magazine letters; ensure enough of each for the note.
# syntax_hint: |
# from collections import Counter; return not (Counter(note) - Counter(mag))


def can_build(note: str, mag: str) -> bool:
    pass


def run_tests() -> None:
    assert can_build("aa", "ab") is False
    assert can_build("aa", "aab") is True
    assert can_build("", "a") is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
