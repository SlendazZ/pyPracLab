from rich.syntax import Syntax

def code_block(code: str) -> Syntax:
    return Syntax(code, 'python')
