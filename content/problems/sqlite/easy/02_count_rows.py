# title: Count Rows
# track: sqlite
# difficulty: easy
# tags: sqlite, sql
# description: |
# Create an in-memory db, insert the given integers into a table 'nums(val)', and return COUNT(*).
# examples:
# count_rows([1, 2, 3]) -> 3
# hint: |
# SELECT COUNT(*) returns one row; fetchone()[0].
# syntax_hint: |
# conn.execute('SELECT COUNT(*) FROM nums').fetchone()[0]


def count_rows(values: list[int]) -> int:
    pass


def run_tests() -> None:
    assert count_rows([1, 2, 3]) == 3
    assert count_rows([]) == 0
    assert count_rows([5]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
