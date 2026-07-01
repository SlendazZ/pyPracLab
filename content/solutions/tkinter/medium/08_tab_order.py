import tkinter  # noqa: F401

def tab_order(names: list[str]) -> list[dict]:
    return [{'name': n, 'tab_index': i} for i, n in enumerate(names)]
