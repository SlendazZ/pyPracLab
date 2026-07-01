import tkinter  # noqa: F401

def buttons(pairs: list[tuple[str, str]]) -> list[dict]:
    return [{'text': l, 'command': c} for l, c in pairs]
