# title: Canvas Coordinates
# track: tkinter
# difficulty: easy
# tags: tkinter, canvas
# description: |
# Given (x1,y1,x2,y2), return canvas rect spec dict with coords and outline 'black'.
# examples:
# rect_spec(0,0,10,10) -> {'coords':(0,0,10,10),'outline':'black'}
# hint: |
# Return plain dict with coords tuple.
# syntax_hint: |
# return {'coords': (x1, y1, x2, y2), 'outline': 'black'}


def rect_spec(x1: int, y1: int, x2: int, y2: int) -> dict:
    pass


def run_tests() -> None:
    assert rect_spec(0, 0, 10, 10) == {'coords': (0, 0, 10, 10), 'outline': 'black'}
    assert rect_spec(1, 2, 3, 4)['coords'] == (1, 2, 3, 4)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
