# title: Directory Size
# track: automations
# difficulty: easy
# tags: pathlib
# description: |
# Given a directory Path, return the total size in bytes of all files recursively.
# examples:
# dir_size(path) -> int
# hint: |
# path.rglob('*') yields all paths; sum file sizes.
# syntax_hint: |
# sum(p.stat().st_size for p in d.rglob('*') if p.is_file())


def dir_size(d) -> int:
    pass


def run_tests() -> None:
    import tempfile, os
    from pathlib import Path
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / 'a.txt').write_text('12')  # 2 bytes
        sub = root / 'sub'
        sub.mkdir()
        (sub / 'b.txt').write_text('abc')  # 3 bytes
        assert dir_size(root) == 5
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
