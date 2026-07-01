# title: Parse Style Color
# track: rich
# difficulty: medium
# tags: rich, style
# description: |
# Given 'bold red' style string, return a rich.style.Style with bold True and color red.
# examples:
# parse_style('bold red') -> Style
# hint: |
# Style.parse('bold red')
# syntax_hint: |
# from rich.style import Style; Style.parse(s)


def parse_style(s: str):
    pass


def run_tests() -> None:
    from rich.style import Style
    st = parse_style('bold red')
    assert isinstance(st, Style)
    assert st.bold is True
    assert 'red' in str(st.color).lower()
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
