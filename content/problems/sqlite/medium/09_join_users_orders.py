# title: Join Users and Orders
# track: sqlite
# difficulty: medium
# tags: sqlite, join
# description: |
# In-memory DB: users(id,name), orders(user_id,amount). Insert data and return (name, total_amount) per user.
# examples:
# totals([('a',10),('a',5),('b',3)]) -> [('a',15),('b',3)]
# hint: |
# JOIN + GROUP BY + SUM.
# syntax_hint: |
# SELECT u.name, SUM(o.amount) ... GROUP BY u.id


def totals(rows: list[tuple[str, float]]) -> list[tuple[str, float]]:
    pass


def run_tests() -> None:
    out = totals([('a', 10), ('a', 5), ('b', 3)])
    assert sorted(out) == [('a', 15.0), ('b', 3.0)]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
