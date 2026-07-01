# title: JSON Syntax Highlight
# track: rich
# difficulty: medium
# tags: rich, json
# description: |
# Return a rich.syntax.Syntax object for JSON text with lexer 'json'.
# examples:
# json_syntax('{"a":1}') -> Syntax instance
# hint: |
# Syntax(code, 'json', theme='monokai')
# syntax_hint: |
# from rich.syntax import Syntax; Syntax(text, 'json')


def json_syntax(text: str):
    pass


def run_tests() -> None:
    from rich.syntax import Syntax
    s = json_syntax('{"a": 1}')
    assert isinstance(s, Syntax)
    assert s.lexer.name.lower() == 'json'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
