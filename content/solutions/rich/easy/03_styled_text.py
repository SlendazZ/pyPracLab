from rich.text import Text

def styled(s: str) -> Text:
    return Text(s, style='bold red')
