# title: Password Strength
# track: apps
# difficulty: easy
# tags: string
# description: |
# Return 'weak' if length < 8, 'medium' if it has >=8 chars and either upper or digit, 'strong' if it has >=8 chars, an upper, and a digit.
# examples:
# strength("abc") -> "weak"
# strength("Abcdefg1") -> "strong"
# hint: |
# Check length, then any(c.isupper()), any(c.isdigit()).
# syntax_hint: |
# has_upper = any(c.isupper() for c in p)


def strength(p: str) -> str:
    pass


def run_tests() -> None:
    assert strength("abc") == "weak"
    assert strength("abcdefgh") == "medium"
    assert strength("abcdefg1") == "medium"
    assert strength("Abcdefg1") == "strong"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
