# title: Color Specs
# track: tkinter
# difficulty: easy
# tags: tkinter, color
# description: |
# Given a list of (label, hex_color), validate and return specs whose 'bg' is the hex color only if it matches #RRGGBB, else 'white'.
# examples:
# color_specs([("a","#ff0000"),("b","nope")]) -> [{"label":"a","bg":"#ff0000"},{"label":"b","bg":"white"}]
# hint: |
# re.fullmatch(r'#[0-9a-fA-F]{6}', color).
# syntax_hint: |
# re.fullmatch(r'#[0-9a-fA-F]{6}', color) is not None


def color_specs(items: list[tuple[str, str]]) -> list[dict]:
    pass


def run_tests() -> None:
    assert color_specs([('a', '#ff0000'), ('b', 'nope')]) == [
        {'label': 'a', 'bg': '#ff0000'},
        {'label': 'b', 'bg': 'white'},
    ]
    assert color_specs([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
