# title: Table Info Columns
# track: sqlite
# difficulty: medium
# tags: sqlite, pragma
# description: |
# Create table with given column definitions dict name->type; return column names via PRAGMA table_info.
# examples:
# table_columns({'id':'INTEGER','name':'TEXT'}) -> ['id','name']
# hint: |
# CREATE TABLE then PRAGMA table_info(t)
# syntax_hint: |
# PRAGMA table_info(users); row[1] is column name


def table_columns(columns: dict[str, str]) -> list[str]:
    pass


def run_tests() -> None:
    cols = table_columns({'id': 'INTEGER', 'name': 'TEXT'})
    assert cols == ['id', 'name']
    assert table_columns({'x': 'REAL'}) == ['x']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
