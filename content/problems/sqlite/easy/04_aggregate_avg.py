# title: Average via SQL
# track: sqlite
# difficulty: easy
# tags: sqlite, sql
# description: |
# Insert the given values into nums(val) and return AVG(val) as a float (0.0 for empty).
# examples:
# average([2, 4, 6]) -> 4.0
# hint: |
# SELECT AVG(val); fetchone()[0] is None when empty.
# syntax_hint: |
# conn.execute('SELECT AVG(val) FROM nums').fetchone()[0]


def average(values: list[int]) -> float:
    pass


def run_tests() -> None:
    assert average([2, 4, 6]) == 4.0
    assert average([10]) == 10.0
    assert average([]) == 0.0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
