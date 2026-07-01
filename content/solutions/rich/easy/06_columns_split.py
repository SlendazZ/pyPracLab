from rich.columns import Columns
from rich.text import Text

def columns(items: list[str]) -> Columns:
    return Columns([Text(s) for s in items])
