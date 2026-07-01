# title: Justify Text
# track: rich
# difficulty: easy
# tags: rich, text
# description: |
# Return a rich.align.Align renderable centering the string in the given width.
# examples:
# justify_line('hi', 20) -> Align center renderable
# hint: |
# Use rich.align.Align.center(s, width=width).
# syntax_hint: |
# from rich.align import Align; Align.center(s, width=width)


def justify_line(s: str, width: int = 20):
    pass


def run_tests() -> None:
    from rich.align import Align
    t = justify_line('hi', 20)
    assert isinstance(t, Align)
    assert t.renderable == 'hi'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
