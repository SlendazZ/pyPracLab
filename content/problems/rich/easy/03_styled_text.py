# title: Styled Text
# track: rich
# difficulty: easy
# tags: rich, text
# description: |
# Return a rich.text.Text with the given string styled 'bold red'.
# examples:
# styled('hi') -> Text with style bold red
# hint: |
# Text(string, style='bold red').
# syntax_hint: |
# from rich.text import Text; Text(s, style='bold red')


def styled(s: str) -> object:
    pass


def run_tests() -> None:
    from rich.text import Text
    t = styled('hi')
    assert isinstance(t, Text)
    assert str(t) == 'hi'
    assert 'red' in str(t.style) and 'bold' in str(t.style)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
