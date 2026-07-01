import tkinter  # noqa: F401

def bind_spec(widget: str, sequence: str, handler: str) -> dict:
    return {'widget': widget, 'sequence': sequence, 'handler': handler}
