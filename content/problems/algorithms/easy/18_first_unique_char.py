# title: First Unique Character
# track: algorithms
# difficulty: easy
# tags: hash-map, string
# description: |
# Return the index of the first non-repeating character in s, or -1.
# examples:
# first_unique("leetcode") -> 0
# first_unique("aabb") -> -1
# hint: |
# Count characters, then find the first with count 1.
# syntax_hint: |
# counts = Counter(s); for i, ch in enumerate(s): if counts[ch]==1: return i


def first_unique(s: str) -> int:
    pass


def run_tests() -> None:
    assert first_unique("leetcode") == 0
    assert first_unique("loveleetcode") == 2
    assert first_unique("aabb") == -1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
