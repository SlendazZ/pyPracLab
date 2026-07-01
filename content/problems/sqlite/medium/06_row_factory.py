# title: Row Factory
# track: sqlite
# difficulty: medium
# tags: sqlite, sql
# description: |
# Create an in-memory db with users(id, name), insert the given names, and return rows as dicts using sqlite3.Row (ordered by name).
# examples:
# as_dicts(['a','b']) -> [{'id':1,'name':'a'},{'id':2,'name':'b'}]
# hint: |
# Set conn.row_factory = sqlite3.Row; dict(row) gives a dict.
# syntax_hint: |
# conn.row_factory = sqlite3.Row; [dict(r) for r in rows]


def as_dicts(names: list[str]) -> list[dict]:
    pass


def run_tests() -> None:
    out = as_dicts(['a', 'b'])
    assert out == [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]
    assert as_dicts([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
