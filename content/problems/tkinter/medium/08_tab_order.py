# title: Tab Order
# track: tkinter
# difficulty: medium
# tags: tkinter, focus
# description: |
# Given widget names in tab order, return list of dicts {name, tab_index}.
# examples:
# tab_order(['a','b']) -> [{'name':'a','tab_index':0},...]
# hint: |
# Enumerate names.
# syntax_hint: |
# [{'name': n, 'tab_index': i} for i, n in enumerate(names)]


def tab_order(names: list[str]) -> list[dict]:
    pass


def run_tests() -> None:
    assert tab_order(['a','b']) == [{'name':'a','tab_index':0},{'name':'b','tab_index':1}]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
