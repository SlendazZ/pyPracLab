# title: Create, Insert, Query
# track: sqlite
# difficulty: easy
# tags: sqlite, sql
# description: |
# Create an in-memory sqlite3 db with table users(id INTEGER PRIMARY KEY, name TEXT), insert the given names, and return (id, name) rows ordered by name.
# examples:
# query_users(["bob", "alice"]) -> [(2, "alice"), (1, "bob")]
# hint: |
# sqlite3.connect(':memory:'); CREATE, INSERT, SELECT; fetchall().
# syntax_hint: |
# conn.execute('SELECT id, name FROM users ORDER BY name').fetchall()


def query_users(names: list[str]) -> list[tuple]:
    pass


def run_tests() -> None:
    assert query_users(["bob", "alice"]) == [(2, "alice"), (1, "bob")]
    assert query_users([]) == []
    assert query_users(["zoe"]) == [(1, "zoe")]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
