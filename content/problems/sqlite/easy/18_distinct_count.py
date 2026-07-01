# title: Distinct Count
# track: sqlite
# difficulty: easy
# tags: sqlite, sql
# description: |
# Insert values into tags(name); return COUNT(DISTINCT name).
# examples:
# distinct_count(['a','b','a']) -> 2
# hint: |
# SELECT COUNT(DISTINCT name) FROM tags
# syntax_hint: |
# COUNT(DISTINCT name)


def distinct_count(names: list[str]) -> int:
    pass


def run_tests() -> None:
    assert distinct_count(['a', 'b', 'a']) == 2
    assert distinct_count([]) == 0
    assert distinct_count(['x']) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
