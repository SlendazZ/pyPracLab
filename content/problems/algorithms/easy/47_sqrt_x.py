# title: Integer Square Root
# track: algorithms
# difficulty: easy
# tags: binary-search, math
# description: |
# Given a non-negative integer x, return the largest integer whose square is less than or equal to x.
# examples:
# sqrt_x(8) -> 2; sqrt_x(16) -> 4
# hint: |
# Binary search on the answer range [0, x]; check mid * mid against x.
# syntax_hint: |
# lo, hi = 0, x; while lo <= hi: mid = (lo + hi) // 2


def sqrt_x(x: int) -> int:
    pass


def run_tests() -> None:
    assert sqrt_x(8) == 2
    assert sqrt_x(16) == 4
    assert sqrt_x(0) == 0
    assert sqrt_x(1) == 1
    assert sqrt_x(15) == 3
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
