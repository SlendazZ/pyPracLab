# title: Group Anagrams
# track: algorithms
# difficulty: medium
# tags: hash-map, string
# description: |
# Group the strings that are anagrams of each other. Return a list of groups (any order).
# examples:
# group(["eat","tea","tan","ate","nat","bat"]) -> [["eat","tea","ate"],["tan","nat"],["bat"]]
# hint: |
# Key each word by its sorted-tuple of characters.
# syntax_hint: |
# key = tuple(sorted(w)); defaultdict(list).append(w)


def group(words: list[str]) -> list[list[str]]:
    pass


def run_tests() -> None:
    r = group(["eat", "tea", "tan", "ate", "nat", "bat"])
    r = sorted(sorted(g) for g in r)
    assert r == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert group([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
