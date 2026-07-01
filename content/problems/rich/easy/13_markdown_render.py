# title: Markdown Render
# track: rich
# difficulty: easy
# tags: rich, markdown
# description: |
# Render markdown text to a string using rich.markdown.Markdown and Console with StringIO.
# examples:
# render_md('# Hi') -> string containing 'Hi'
# hint: |
# Markdown(text); Console(file=StringIO()).print(md)
# syntax_hint: |
# from rich.markdown import Markdown; from rich.console import Console


def render_md(text: str) -> str:
    pass


def run_tests() -> None:
    s = render_md('# Hello')
    assert 'Hello' in s
    assert render_md('plain') != ''
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
