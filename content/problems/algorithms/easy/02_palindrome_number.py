# title: Palindrome Number
# track: algorithms
# difficulty: easy
# tags: math
# description: |
# Return True if the integer reads the same forwards and backwards, without converting it to a string. Negative numbers are not palindromes.
# examples:
# is_palindrome(121) -> True
# is_palindrome(-121) -> False
# hint: |
# Reverse half of the number by repeatedly taking x % 10 and building a reversed value.
# syntax_hint: |
# while x > reversed_half: reversed_half = reversed_half * 10 + x % 10; x //= 10


def is_palindrome(x: int) -> bool:
    pass


def run_tests() -> None:
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
    assert is_palindrome(0) is True
    assert is_palindrome(1221) is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
