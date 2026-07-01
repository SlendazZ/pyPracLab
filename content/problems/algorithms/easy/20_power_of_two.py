# title: Power of Two
# track: algorithms
# difficulty: easy
# tags: bit-manipulation, math
# description: |
# Return True if n is a power of two.
# examples:
# is_power_of_two(16) -> True
# is_power_of_two(3) -> False
# hint: |
# A power of two has exactly one bit set: n > 0 and (n & (n-1)) == 0.
# syntax_hint: |
# return n > 0 and (n & (n - 1)) == 0


def is_power_of_two(n: int) -> bool:
    pass


def run_tests() -> None:
    assert is_power_of_two(16) is True
    assert is_power_of_two(3) is False
    assert is_power_of_two(1) is True
    assert is_power_of_two(0) is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
