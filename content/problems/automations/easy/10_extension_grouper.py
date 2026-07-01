# title: Extension Grouper
# track: automations
# difficulty: easy
# tags: pathlib, collections
# description: |
# Given a list of filenames, group them by file extension into a dict ext -> list of names.
# examples:
# group_ext(["a.txt","b.txt","c.md"]) -> {"txt":["a.txt","b.txt"],"md":["c.md"]}
# hint: |
# Path(name).suffix gives the extension.
# syntax_hint: |
# from pathlib import Path; ext = Path(name).suffix


def group_ext(names: list[str]) -> dict[str, list[str]]:
    pass


def run_tests() -> None:
    assert group_ext(["a.txt", "b.txt", "c.md"]) == {"txt": ["a.txt", "b.txt"], "md": ["c.md"]}
    assert group_ext([]) == {}
    assert group_ext(["noext"]) == {"": ["noext"]}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
