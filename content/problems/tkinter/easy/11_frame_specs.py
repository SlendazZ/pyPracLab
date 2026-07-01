# title: Frame Specs
# track: tkinter
# difficulty: easy
# tags: tkinter, frame
# description: |
# Given list of frame names, return specs dicts with name, relief 'groove', borderwidth 2.
# examples:
# frame_specs(['main']) -> [{'name':'main','relief':'groove','borderwidth':2}]
# hint: |
# List comprehension building dicts.
# syntax_hint: |
# [{'name': n, 'relief': 'groove', 'borderwidth': 2} for n in names]


def frame_specs(names: list[str]) -> list[dict]:
    pass


def run_tests() -> None:
    assert frame_specs(['main']) == [{'name': 'main', 'relief': 'groove', 'borderwidth': 2}]
    assert frame_specs([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
