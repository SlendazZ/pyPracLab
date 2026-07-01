# title: Set Comprehension - Vowels
# track: syntax
# difficulty: easy
# tags: comprehension, set
# description: |
# Return the set of vowels present in a string (case-insensitive), using a set comprehension.
# examples:
# vowels("Hello World") -> {"e","o"}
# hint: |
# {ch for ch in text.lower() if ch in 'aeiou'}
# syntax_hint: |
# set comprehension: {expr for ... if ...}


def vowels(text: str) -> set[str]:
    pass


def run_tests() -> None:
    assert vowels("Hello World") == {"e", "o"}
    assert vowels("sky") == set()
    assert vowels("AEI") == {"a", "e", "i"}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
