# title: Truncate Preview
# track: automations
# difficulty: easy
# tags: string
# description: |
# Return a one-line preview of text: collapse whitespace and truncate to max chars, adding '...' if cut.
# examples:
# preview("hello   world", 8) -> "hello..."
# hint: |
# ' '.join(text.split()) collapses all whitespace.
# syntax_hint: |
# if len(s) > n: s = s[:n-3] + '...'


def preview(text: str, n: int) -> str:
    pass


def run_tests() -> None:
    assert preview("hello   world", 8) == "hello..."
    assert preview("hi", 10) == "hi"
    assert preview("abcdefgh", 5) == "ab..."
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
