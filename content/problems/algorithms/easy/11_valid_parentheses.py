# title: Valid Parentheses
# track: algorithms
# difficulty: easy
# tags: stack
# description: |
# Return True if the string of '()[]{}' is valid: every opener is closed by the same type in the correct order.
# examples:
# is_valid("()[]{}") -> True
# is_valid("(]") -> False
# hint: |
# Push openers on a stack; on a closer, check the top matches.
# syntax_hint: |
# pairs = {')': '(', ']': '[', '}': '{'}; stack.append or pop


def is_valid(s: str) -> bool:
    pass


def run_tests() -> None:
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
