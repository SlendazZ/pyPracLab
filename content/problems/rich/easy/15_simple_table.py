# title: Simple Data Table
# track: rich
# difficulty: easy
# tags: rich, table
# description: |
# Build a Table with columns Name and Value and one row from the given name/value pair.
# examples:
# pair_table('x', '1') -> Table with 1 row
# hint: |
# Table(); add_column twice; add_row(name, value)
# syntax_hint: |
# table.add_column('Name'); table.add_row(name, value)


def pair_table(name: str, value: str):
    pass


def run_tests() -> None:
    from rich.table import Table
    t = pair_table('x', '1')
    assert isinstance(t, Table)
    assert len(t.columns) == 2
    assert len(t.rows) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
