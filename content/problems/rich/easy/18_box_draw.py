# title: Box Panel
# track: rich
# difficulty: easy
# tags: rich, panel
# description: |
# Return a Panel around text using box style ROUNDED.
# examples:
# box_panel('msg') -> Panel with ROUNDED box
# hint: |
# Panel(text, box=box.ROUNDED)
# syntax_hint: |
# from rich.panel import Panel; from rich import box; Panel(s, box=box.ROUNDED)


def box_panel(text: str):
    pass


def run_tests() -> None:
    from rich.panel import Panel
    from rich import box
    p = box_panel('msg')
    assert isinstance(p, Panel)
    assert p.box == box.ROUNDED
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
