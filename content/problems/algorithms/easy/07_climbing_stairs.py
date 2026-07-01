# title: Climbing Stairs
# track: algorithms
# difficulty: easy
# tags: dp
# description: |
# You can climb 1 or 2 stairs at a time. Return the number of distinct ways to climb n stairs.
# examples:
# climb(2) -> 2
# climb(3) -> 3
# hint: |
# It's the Fibonacci sequence: ways(n) = ways(n-1) + ways(n-2).
# syntax_hint: |
# a, b = 1, 1; for _ in range(n): a, b = b, a + b


def climb(n: int) -> int:
    pass


def run_tests() -> None:
    assert climb(1) == 1
    assert climb(2) == 2
    assert climb(3) == 3
    assert climb(5) == 8
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
