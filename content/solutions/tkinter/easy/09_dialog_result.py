import tkinter  # noqa: F401

def dialog_result(label: str) -> bool | None:
    m = {'ok': True, 'cancel': False}
    return m.get(label.lower())
