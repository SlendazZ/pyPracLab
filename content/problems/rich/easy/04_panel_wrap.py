# title: Wrap in a Panel
# track: rich
# difficulty: easy
# tags: rich, panel
# description: |
# Return a rich.panel.Panel titled with the given title wrapping the given text.
# examples:
# wrap('body', 'Title') -> Panel
# hint: |
# Panel(text, title=title).
# syntax_hint: |
# from rich.panel import Panel; Panel(text, title=title)


def wrap(text: str, title: str) -> object:
    pass


def run_tests() -> None:
    from rich.panel import Panel
    p = wrap('body', 'Title')
    assert isinstance(p, Panel)
    assert p.title == 'Title'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
