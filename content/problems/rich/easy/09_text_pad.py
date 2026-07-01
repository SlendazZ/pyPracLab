# title: Pad Text
# track: rich
# difficulty: easy
# tags: rich, text
# description: |
# Return a rich.text.Text with the string padded to width with spaces on the right.
# examples:
# pad_text('hi', 5) -> Text 'hi   '
# hint: |
# Text(s.ljust(width))
# syntax_hint: |
# from rich.text import Text; Text(s.ljust(width))


def pad_text(s: str, width: int) -> object:
    pass


def run_tests() -> None:
    from rich.text import Text
    t = pad_text('hi', 5)
    assert isinstance(t, Text)
    assert str(t) == 'hi   '
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
