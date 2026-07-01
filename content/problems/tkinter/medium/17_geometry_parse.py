# title: Geometry Parse
# track: tkinter
# difficulty: medium
# tags: tkinter, geometry
# description: |
# Parse geometry string 'WxH+X+Y' into dict with width, height, x, y ints.
# examples:
# parse_geometry('400x300+10+20') -> {'width':400,'height':300,'x':10,'y':20}
# hint: |
# Regex or split on x and +.
# syntax_hint: |
# import re; match WxH+X+Y pattern


def parse_geometry(s: str) -> dict:
    pass


def run_tests() -> None:
    assert parse_geometry('400x300+10+20') == {'width': 400, 'height': 300, 'x': 10, 'y': 20}
    assert parse_geometry('100x50+0+0')['width'] == 100
    assert parse_geometry('800x600+5+15')['y'] == 15
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
