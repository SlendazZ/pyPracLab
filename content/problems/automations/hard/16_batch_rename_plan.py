# title: Batch Rename Plan
# track: automations
# difficulty: hard
# tags: files
# description: |
# Given filenames and a prefix, return list of (old, new) rename pairs adding zero-padded index: prefix_001.ext.
# examples:
# plan(["a.txt","b.txt"], "img") -> [("a.txt","img_001.txt"),("b.txt","img_002.txt")]
# hint: |
# Enumerate starting at 1; keep extension from old name.
# syntax_hint: |
# from pathlib import Path; Path(name).suffix


def plan(names: list[str], prefix: str) -> list[tuple[str, str]]:
    pass


def run_tests() -> None:
    assert plan(["a.txt","b.txt"], "img") == [("a.txt","img_001.txt"),("b.txt","img_002.txt")]
    assert plan([], "x") == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
