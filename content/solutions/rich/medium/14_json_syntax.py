from rich.syntax import Syntax

def json_syntax(text: str):
    return Syntax(text, 'json', theme='monokai')
