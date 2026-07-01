# title: All Pairs
# track: syntax
# difficulty: easy
# tags: itertools
# description: |
# Return all 2-element combinations from items as sorted tuples (order within tuple sorted).
# examples:
# all_pairs([1,2,3]) -> [(1,2),(1,3),(2,3)]
# hint: |
# itertools.combinations(items, 2)
# syntax_hint: |
# from itertools import combinations; sorted(combinations(items, 2))


def all_pairs(items: list) -> list[tuple]:
    pass


def run_tests() -> None:
    assert all_pairs([1,2,3]) == [(1,2),(1,3),(2,3)]
    assert all_pairs(['a']) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
