# title: WHERE Filter
# track: sqlite
# difficulty: easy
# tags: sqlite, sql
# description: |
# Create an in-memory db with nums(val), insert the values, and return those strictly greater than threshold (ascending).
# examples:
# above([1, 5, 2, 7], 3) -> [5, 7]
# hint: |
# SELECT val FROM nums WHERE val > ? ORDER BY val.
# syntax_hint: |
# conn.execute('SELECT val FROM nums WHERE val > ? ORDER BY val', (threshold,))


def above(values: list[int], threshold: int) -> list[int]:
    pass


def run_tests() -> None:
    assert above([1, 5, 2, 7], 3) == [5, 7]
    assert above([1, 2], 5) == []
    assert above([], 0) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
