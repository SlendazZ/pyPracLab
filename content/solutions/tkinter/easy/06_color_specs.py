import re
import tkinter  # noqa: F401

def color_specs(items: list[tuple[str, str]]) -> list[dict]:
    out = []
    for label, color in items:
        bg = color if re.fullmatch(r'#[0-9a-fA-F]{6}', color) else 'white'
        out.append({'label': label, 'bg': bg})
    return out
