import tkinter  # noqa: F401

def rect_spec(x1: int, y1: int, x2: int, y2: int) -> dict:
    return {'coords': (x1, y1, x2, y2), 'outline': 'black'}
