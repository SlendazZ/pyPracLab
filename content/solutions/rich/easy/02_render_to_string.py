import io
from rich.console import Console

def render(renderable) -> str:
    buf = io.StringIO()
    console = Console(file=buf, width=80, force_terminal=False)
    console.print(renderable)
    return buf.getvalue()
