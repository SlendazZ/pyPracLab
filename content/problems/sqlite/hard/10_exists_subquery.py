# title: EXISTS Subquery
# track: sqlite
# difficulty: hard
# tags: sqlite
# description: |
# Given names, insert into users and return names that have at least one order.
# examples:
# with_orders([('a',True),('b',False)]) -> ['a']
# hint: |
# WHERE EXISTS (SELECT 1 FROM orders ...).
# syntax_hint: |
# SELECT name FROM users u WHERE EXISTS (...)


def with_orders(entries: list[tuple[str, bool]]) -> list[str]:
    pass


def run_tests() -> None:
    assert with_orders([('a', True), ('b', False)]) == ['a']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
