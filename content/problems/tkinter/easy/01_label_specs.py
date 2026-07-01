# title: Tkinter Label Specs
# track: tkinter
# difficulty: easy
# tags: tkinter, dict
# description: |
# Given a list of (key, text) pairs, return label specs: dicts like {"key": key, "text": text, "anchor": "w"}.
# examples:
# label_specs([("name", "Name:")]) -> [{"key":"name","text":"Name:","anchor":"w"}]
# hint: |
# A list comprehension building dicts is all you need here.
# syntax_hint: |
# [{"key": k, "text": t, "anchor": "w"} for k, t in pairs]


def label_specs(pairs: list[tuple[str, str]]) -> list[dict]:
    pass


def run_tests() -> None:
    assert label_specs([("name", "Name:")]) == [{"key": "name", "text": "Name:", "anchor": "w"}]
    assert label_specs([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
