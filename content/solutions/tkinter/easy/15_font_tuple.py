import tkinter  # noqa: F401

def font_tuple(family: str, size: int, style: str = '') -> tuple:
    return (family, size, style or '')
