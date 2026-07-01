import tkinter  # noqa: F401

def frame_specs(names: list[str]) -> list[dict]:
    return [{'name': n, 'relief': 'groove', 'borderwidth': 2} for n in names]
