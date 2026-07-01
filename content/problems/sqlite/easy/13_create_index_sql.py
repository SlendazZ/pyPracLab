# title: Create Index SQL
# track: sqlite
# difficulty: easy
# tags: sqlite, sql
# description: |
# Return the SQL string to create index idx_name on table users(column name).
# examples:
# index_sql('users', 'name') -> 'CREATE INDEX ...'
# hint: |
# Static f-string with CREATE INDEX IF NOT EXISTS.
# syntax_hint: |
# CREATE INDEX IF NOT EXISTS idx_{table}_{col} ON {table}({col})


def index_sql(table: str, column: str) -> str:
    pass


def run_tests() -> None:
    s = index_sql('users', 'name')
    assert 'CREATE INDEX' in s.upper()
    assert 'users' in s and 'name' in s
    assert index_sql('t', 'x') == index_sql('t', 'x')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
