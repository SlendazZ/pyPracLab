# title: Join with Columns
# track: rich
# difficulty: easy
# tags: rich, columns
# description: |
# Return a rich.columns.Columns containing one rich.text.Text per given string.
# examples:
# columns(['a','b']) -> Columns with 2 renderables
# hint: |
# Columns([Text(s) for s in items]).
# syntax_hint: |
# from rich.columns import Columns; Columns([Text(s) for s in items])


def columns(items: list[str]) -> object:
    pass


def run_tests() -> None:
    from rich.columns import Columns
    c = columns(['a', 'b'])
    assert isinstance(c, Columns)
    assert len(c.renderables) == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
