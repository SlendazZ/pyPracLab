from rich.text import Text

def pad_text(s: str, width: int) -> Text:
    return Text(s.ljust(width))
