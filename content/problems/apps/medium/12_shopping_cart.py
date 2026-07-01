# title: Shopping Cart Total
# track: apps
# difficulty: medium
# tags: class
# description: |
# Cart stores (name, price, qty) items; total() sums price*qty.
# examples:
# c.add('apple', 1.0, 3); c.total() -> 3.0
# hint: |
# List of tuples or small dicts.
# syntax_hint: |
# sum(price * qty for ...)


class Cart:
    def __init__(self): pass
    def add(self, name: str, price: float, qty: int) -> None: pass
    def total(self) -> float: pass


def run_tests() -> None:
    c = Cart()
    c.add('apple', 1.0, 3)
    c.add('bread', 2.5, 1)
    assert c.total() == 5.5
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
