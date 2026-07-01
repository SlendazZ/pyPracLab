# title: Inventory Total Value
# track: apps
# difficulty: easy
# tags: dict
# description: |
# Given an inventory dict {item: (quantity, unit_price)} return the total value.
# examples:
# total_value({'a': (2, 5), 'b': (1, 10)}) -> 20
# hint: |
# Sum qty * price for each item.
# syntax_hint: |
# sum(q * p for q, p in inv.values())


def total_value(inv: dict) -> float:
    pass


def run_tests() -> None:
    assert total_value({'a': (2, 5), 'b': (1, 10)}) == 20
    assert total_value({}) == 0
    assert total_value({'x': (3, 2.5)}) == 7.5
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
