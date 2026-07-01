# title: GROUP BY HAVING
# track: sqlite
# difficulty: medium
# tags: sqlite, sql
# description: |
# Create in-memory db, insert (dept, sales) rows, return depts with SUM(sales) > threshold.
# examples:
# depts_over(rows, 100) -> list of dept names
# hint: |
# GROUP BY dept HAVING SUM(sales) > ?
# syntax_hint: |
# SELECT dept FROM t GROUP BY dept HAVING SUM(sales) > ?


def depts_over(rows: list[tuple[str, int]], threshold: int) -> list[str]:
    pass


def run_tests() -> None:
    rows = [('a', 50), ('a', 60), ('b', 30)]
    assert depts_over(rows, 100) == ['a']
    assert depts_over(rows, 200) == []
    assert depts_over([], 0) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
