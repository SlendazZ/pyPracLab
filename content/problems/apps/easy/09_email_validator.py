# title: Email Validator
# track: apps
# difficulty: easy
# tags: regex
# description: |
# Return True if a string is a plausible email: one '@', a local part, a domain with a dot.
# examples:
# is_email("a@b.com") -> True
# is_email("nope") -> False
# hint: |
# A simple regex: local@domain.tld with no spaces.
# syntax_hint: |
# re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', s)


def is_email(s: str) -> bool:
    pass


def run_tests() -> None:
    assert is_email("a@b.com") is True
    assert is_email("eli.test@site.io") is True
    assert is_email("nope") is False
    assert is_email("a @b.com") is False
    assert is_email("a@b") is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
