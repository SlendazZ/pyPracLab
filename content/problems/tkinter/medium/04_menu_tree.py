# title: Menu Tree Builder
# track: tkinter
# difficulty: medium
# tags: tkinter, menu
# description: |
# Given a nested spec like {'File': {'Open': None, 'Quit': None}, 'Help': {}}, return a flat list of (label_path) strings like 'File > Open', 'File > Quit'. Items with a non-empty dict recurse; None means a leaf.
# examples:
# paths({'File': {'Open': None}}) -> ['File > Open']
# hint: |
# Recurse, joining the current label with ' > '.
# syntax_hint: |
# if value is None: append(path) else: recurse(value, path)


def paths(spec: dict) -> list[str]:
    pass


def run_tests() -> None:
    spec = {'File': {'Open': None, 'Quit': None}, 'Help': {'About': None}}
    assert sorted(paths(spec)) == ['File > Open', 'File > Quit', 'Help > About']
    assert paths({}) == []
    assert paths({'X': None}) == ['X']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
