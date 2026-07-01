# title: Valid Palindrome
# track: algorithms
# difficulty: easy
# tags: two-pointers, string
# description: |
# Return True if a string is a palindrome after considering only alphanumeric characters and ignoring case.
# examples:
# valid_palindrome("A man, a plan, a canal: Panama") -> True
# hint: |
# Two pointers from both ends; skip non-alphanumeric chars and compare lowered letters.
# syntax_hint: |
# while left < right: advance past non-alnum; compare s[left].lower()


def valid_palindrome(s: str) -> bool:
    pass


def run_tests() -> None:
    assert valid_palindrome("A man, a plan, a canal: Panama") is True
    assert valid_palindrome("race a car") is False
    assert valid_palindrome(" ") is True
    assert valid_palindrome("0P") is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
