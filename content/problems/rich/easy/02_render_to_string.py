# title: Render to a String
# track: rich
# difficulty: easy
# tags: rich, console
# description: |
# Render a given rich renderable to a string (no terminal) using Console with StringIO and width 80.
# examples:
# render(table) -> str containing the table text
# hint: |
# Console(file=io.StringIO(), width=80, force_terminal=False); console.print(x).
# syntax_hint: |
# from rich.console import Console; import io; buf=io.StringIO()


def render(renderable) -> str:
    pass


def run_tests() -> None:
    from rich.text import Text
    s = render(Text('hello'))
    assert 'hello' in s
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
