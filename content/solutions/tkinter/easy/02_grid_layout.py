import tkinter  # noqa: F401

def plan(specs: list[tuple[str, int, int]]) -> list[dict]:
    return [{"widget": n, "row": r, "col": c, "sticky": "ew"} for n, r, c in specs]
