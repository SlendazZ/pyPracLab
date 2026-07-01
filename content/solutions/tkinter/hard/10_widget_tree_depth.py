import tkinter  # noqa: F401

def depth(tree: dict) -> int:
    if not tree:
        return 0
    return 1 + max((depth(v) for v in tree.values()), default=0)
