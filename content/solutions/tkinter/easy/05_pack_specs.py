import tkinter  # noqa: F401

def pack_specs(items: list[tuple[str, str]]) -> list[dict]:
    return [{'widget': w, 'side': s, 'fill': 'x'} for w, s in items]
