import tkinter  # noqa: F401

def is_nonneg(s: str) -> bool:
    return s == '' or s.isdigit()
