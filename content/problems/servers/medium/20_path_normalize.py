# title: Path Normalize
# track: servers
# difficulty: medium
# tags: url, path
# description: |
# Normalize a URL path: collapse //, resolve . and .., ensure leading slash.
# examples:
# normalize('/a/../b/./c') -> '/b/c'
# hint: |
# Split segments; stack-based .. handling.
# syntax_hint: |
# stack append segment; on '..' pop if possible


def normalize(path: str) -> str:
    pass


def run_tests() -> None:
    assert normalize('/a/../b/./c') == '/b/c'
    assert normalize('//a//b//') == '/a/b'
    assert normalize('/x/y/../z') == '/x/z'
    assert normalize('/') == '/'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
