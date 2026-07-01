# title: Build a Rich Table
# track: rich
# difficulty: easy
# tags: rich, table
# description: |
# Given a list of column headers and a list of row tuples, build and return a rich.table.Table with those columns and rows.
# examples:
# build_table(["a","b"], [("1","2")]) -> Table
# hint: |
# from rich.table import Table; add_column / add_row.
# syntax_hint: |
# table = Table(); table.add_column(name); table.add_row(*values)


def build_table(headers: list[str], rows: list[tuple]) -> object:
    pass


def run_tests() -> None:
    from rich.table import Table
    t = build_table(["a", "b"], [("1", "2"), ("3", "4")])
    assert isinstance(t, Table)
    assert len(t.columns) == 2 and len(t.rows) == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
