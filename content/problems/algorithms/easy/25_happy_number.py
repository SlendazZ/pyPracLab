# title: Happy Number
# track: algorithms
# difficulty: easy
# tags: set, math
# description: |
# A happy number repeatedly replaces itself with the sum of the squares of its digits until it reaches 1. Return True if n is happy.
# examples:
# is_happy(19) -> True
# is_happy(2) -> False
# hint: |
# Detect cycles with a set of seen numbers.
# syntax_hint: |
# while n != 1 and n not in seen: seen.add(n); n = sum(int(d)**2 for d in str(n))


def is_happy(n: int) -> bool:
    pass


def run_tests() -> None:
    assert is_happy(19) is True
    assert is_happy(2) is False
    assert is_happy(1) is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
