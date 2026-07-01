import io
from rich.console import Console
from rich.markdown import Markdown

def render_md(text: str) -> str:
    buf = io.StringIO()
    console = Console(file=buf, width=80, force_terminal=False)
    console.print(Markdown(text))
    return buf.getvalue()
