import tkinter  # noqa: F401  (exercises the import; no window opened)

def label_specs(pairs: list[tuple[str, str]]) -> list[dict]:
    return [{"key": k, "text": t, "anchor": "w"} for k, t in pairs]
