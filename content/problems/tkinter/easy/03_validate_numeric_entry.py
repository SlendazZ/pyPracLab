# title: Validate Numeric Entry
# track: tkinter
# difficulty: easy
# tags: tkinter, validation
# description: |
# Return True if the entry text is a non-negative integer (the kind of check a Tk validation command would use).
# examples:
# is_nonneg("123") -> True
# is_nonneg("-1") -> False
# is_nonneg("") -> True
# hint: |
# str.isdigit() is True for non-negative integers and for the empty string is False—handle empty as valid.
# syntax_hint: |
# return s == '' or s.isdigit()


def is_nonneg(s: str) -> bool:
    pass


def run_tests() -> None:
    assert is_nonneg("123") is True
    assert is_nonneg("-1") is False
    assert is_nonneg("") is True
    assert is_nonneg("12a") is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
