# title: Path Parts
# track: syntax
# difficulty: easy
# tags: pathlib
# description: |
# Given a POSIX path string, return (parent, name, suffix) using pathlib.
# examples:
# path_parts('/tmp/data.csv') -> ('/tmp', 'data.csv', '.csv')
# hint: |
# Path(p).parent, .name, .suffix — str(parent) for compare.
# syntax_hint: |
# from pathlib import Path; p = Path(s)


def path_parts(p: str) -> tuple[str, str, str]:
    pass


def run_tests() -> None:
    assert path_parts('/tmp/data.csv') == ('/tmp', 'data.csv', '.csv')
    assert path_parts('file.txt')[1] == 'file.txt'
    assert path_parts('/a/b')[0] == '/a'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
