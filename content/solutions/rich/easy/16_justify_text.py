from rich.align import Align

def justify_line(s: str, width: int = 20):
    return Align.center(s, width=width)
