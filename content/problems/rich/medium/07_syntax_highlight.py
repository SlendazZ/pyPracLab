# title: Syntax Block
# track: rich
# difficulty: medium
# tags: rich, syntax
# description: |
# Return a rich.syntax.Syntax block for the given Python code string with background disabled.
# examples:
# code_block('x = 1') -> Syntax
# hint: |
# Syntax(code, 'python', background='default').
# syntax_hint: |
# from rich.syntax import Syntax; Syntax(code, 'python')


def code_block(code: str) -> object:
    pass


def run_tests() -> None:
    from rich.syntax import Syntax
    s = code_block('x = 1')
    assert isinstance(s, Syntax)
    assert s.code == 'x = 1'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
