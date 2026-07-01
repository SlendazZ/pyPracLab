# title: sorted() with key
# track: syntax
# difficulty: easy
# tags: sorted
# description: |
# Sort a list of strings by length, then alphabetically, using sorted with a key tuple.
# examples:
# sort_len(["bb","a","ccc","b"]) -> ["a","b","bb","ccc"]
# hint: |
# key=lambda s: (len(s), s)
# syntax_hint: |
# sorted(items, key=lambda s: (len(s), s))


def sort_len(words: list[str]) -> list[str]:
    pass


def run_tests() -> None:
    assert sort_len(["bb", "a", "ccc", "b"]) == ["a", "b", "bb", "ccc"]
    assert sort_len(["aaa", "b", "cc"]) == ["b", "cc", "aaa"]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
