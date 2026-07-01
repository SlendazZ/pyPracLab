import re
import tkinter  # noqa: F401

_GEOM = re.compile(r'^(\d+)x(\d+)\+(\d+)\+(\d+)$')

def parse_geometry(s: str) -> dict:
    m = _GEOM.match(s)
    if not m:
        raise ValueError('invalid geometry')
    w, h, x, y = m.groups()
    return {'width': int(w), 'height': int(h), 'x': int(x), 'y': int(y)}
