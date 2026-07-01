# title: Isomorphic Strings
# track: algorithms
# difficulty: easy
# tags: hash-map, string
# description: |
# Two strings are isomorphic if chars in s map 1-1 to chars in t. Return True/False.
# examples:
# isomorphic("egg","add") -> True
# isomorphic("foo","bar") -> False
# hint: |
# Two dicts track s->t and t->s mappings; reject on mismatch.
# syntax_hint: |
# return len(set(zip(s,t))) == len(set(s)) == len(set(t))


def isomorphic(s: str, t: str) -> bool:
    pass


def run_tests() -> None:
    assert isomorphic("egg", "add") is True
    assert isomorphic("foo", "bar") is False
    assert isomorphic("paper", "title") is True
    assert isomorphic("badc", "baba") is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
