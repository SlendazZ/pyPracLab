# title: defaultdict - Group By Length
# track: syntax
# difficulty: easy
# tags: collections
# description: |
# Group words by their length into a dict mapping length -> list of words, using collections.defaultdict.
# examples:
# group_by_len(["a","bb","c","dd"]) -> {1:["a","c"], 2:["bb","dd"]}
# hint: |
# defaultdict(list) auto-creates empty lists.
# syntax_hint: |
# from collections import defaultdict; d = defaultdict(list); d[len(w)].append(w)


def group_by_len(words: list[str]) -> dict[int, list[str]]:
    pass


def run_tests() -> None:
    assert group_by_len(["a", "bb", "c", "dd"]) == {1: ["a", "c"], 2: ["bb", "dd"]}
    assert group_by_len([]) == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
