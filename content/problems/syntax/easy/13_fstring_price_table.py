# title: f-strings - Price Table
# track: syntax
# difficulty: easy
# tags: fstring
# description: |
# Given a list of (name, price) tuples, return lines like 'apple: $1.20' with two decimals using f-strings.
# examples:
# price_table([("apple",1.2)]) -> ["apple: $1.20"]
# hint: |
# f'{name}: ${price:.2f}' formats to two decimals.
# syntax_hint: |
# f'{name}: ${price:.2f}'


def price_table(rows: list[tuple[str, float]]) -> list[str]:
    pass


def run_tests() -> None:
    assert price_table([("apple", 1.2)]) == ["apple: $1.20"]
    assert price_table([("x", 0), ("y", 5)]) == ["x: $0.00", "y: $5.00"]
    assert price_table([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
