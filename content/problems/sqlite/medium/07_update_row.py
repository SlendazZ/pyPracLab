# title: Update a Row
# track: sqlite
# difficulty: medium
# tags: sqlite, sql
# description: |
# Create a people(id, name) table, insert ('1','old'), UPDATE the name to 'new' where id=1, and return the resulting name.
# examples:
# update_name() -> 'new'
# hint: |
# UPDATE people SET name=? WHERE id=?.
# syntax_hint: |
# conn.execute('UPDATE people SET name=? WHERE id=?', ('new', 1))


def update_name() -> str:
    pass


def run_tests() -> None:
    assert update_name() == 'new'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
