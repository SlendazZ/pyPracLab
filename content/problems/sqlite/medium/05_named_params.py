# title: Named Parameters
# track: sqlite
# difficulty: medium
# tags: sqlite, sql
# description: |
# Insert one row with named parameters into a people(name, age) table and return that single row as a dict {name, age}.
# examples:
# insert_one('eli', 30) -> {'name': 'eli', 'age': 30}
# hint: |
# Use :name and :age placeholders and a dict params.
# syntax_hint: |
# conn.execute('INSERT INTO people VALUES (:name, :age)', {'name': name, 'age': age})


def insert_one(name: str, age: int) -> dict:
    pass


def run_tests() -> None:
    assert insert_one('eli', 30) == {'name': 'eli', 'age': 30}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
