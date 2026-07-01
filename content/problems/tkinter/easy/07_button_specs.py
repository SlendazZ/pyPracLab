# title: Button Specs
# track: tkinter
# difficulty: easy
# tags: tkinter
# description: |
# Given (label, command_name) pairs, return button specs with text and command fields.
# examples:
# buttons([("Save","save")]) -> [{"text":"Save","command":"save"}]
# hint: |
# List comprehension building dicts.
# syntax_hint: |
# [{'text': l, 'command': c} for l, c in pairs]


def buttons(pairs: list[tuple[str, str]]) -> list[dict]:
    pass


def run_tests() -> None:
    assert buttons([("Save","save")]) == [{"text":"Save","command":"save"}]
    assert buttons([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
