# title: Grid Layout Planner
# track: tkinter
# difficulty: easy
# tags: tkinter, grid
# description: |
# Given a list of (widget_name, row, col), return a list of dicts {"widget", "row", "col", "sticky": "ew"} ready for grid().
# examples:
# plan([("a", 0, 0)]) -> [{"widget":"a","row":0,"col":0,"sticky":"ew"}]
# hint: |
# Build dicts with the sticky default added.
# syntax_hint: |
# [{"widget": n, "row": r, "col": c, "sticky": "ew"} for n, r, c in specs]


def plan(specs: list[tuple[str, int, int]]) -> list[dict]:
    pass


def run_tests() -> None:
    assert plan([("a", 0, 0), ("b", 0, 1)]) == [
        {"widget": "a", "row": 0, "col": 0, "sticky": "ew"},
        {"widget": "b", "row": 0, "col": 1, "sticky": "ew"},
    ]
    assert plan([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
