from rich import box
from rich.panel import Panel

def box_panel(text: str):
    return Panel(text, box=box.ROUNDED)
