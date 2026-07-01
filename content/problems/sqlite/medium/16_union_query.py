# title: UNION Query
# track: sqlite
# difficulty: medium
# tags: sqlite, sql
# description: |
# Insert names into tables a and b; return sorted unique names from UNION ALL then dedupe in Python, or use UNION.
# examples:
# union_names(['a','b'], ['b','c']) -> ['a','b','c']
# hint: |
# SELECT name FROM a UNION SELECT name FROM b
# syntax_hint: |
# UNION removes duplicates automatically


def union_names(list_a: list[str], list_b: list[str]) -> list[str]:
    pass


def run_tests() -> None:
    assert union_names(['a', 'b'], ['b', 'c']) == ['a', 'b', 'c']
    assert union_names([], ['x']) == ['x']
    assert union_names(['z'], []) == ['z']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
