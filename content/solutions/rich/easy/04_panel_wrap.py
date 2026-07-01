from rich.panel import Panel

def wrap(text: str, title: str) -> Panel:
    return Panel(text, title=title)
