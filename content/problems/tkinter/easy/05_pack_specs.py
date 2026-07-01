# title: Pack Side Specs
# track: tkinter
# difficulty: easy
# tags: tkinter, pack
# description: |
# Given a list of (widget, side) where side is 'top' or 'bottom', return pack specs: {'widget', 'side', 'fill': 'x'}.
# examples:
# pack_specs([('a','top')]) -> [{'widget':'a','side':'top','fill':'x'}]
# hint: |
# A comprehension builds the spec dicts.
# syntax_hint: |
# [{'widget': w, 'side': s, 'fill': 'x'} for w, s in items]


def pack_specs(items: list[tuple[str, str]]) -> list[dict]:
    pass


def run_tests() -> None:
    assert pack_specs([('a', 'top'), ('b', 'bottom')]) == [
        {'widget': 'a', 'side': 'top', 'fill': 'x'},
        {'widget': 'b', 'side': 'bottom', 'fill': 'x'},
    ]
    assert pack_specs([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
