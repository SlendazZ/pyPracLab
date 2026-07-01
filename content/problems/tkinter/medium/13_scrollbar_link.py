# title: Scrollbar Link Spec
# track: tkinter
# difficulty: medium
# tags: tkinter, scrollbar
# description: |
# Given widget and scrollbar names, return link spec dict connecting them for yscrollcommand/xview.
# examples:
# scroll_link('text','scroll') -> dict with command keys
# hint: |
# Map widget yscrollcommand to scrollbar.set pattern as data.
# syntax_hint: |
# return {'widget': w, 'scrollbar': s, 'orient': 'vertical'}


def scroll_link(widget: str, scrollbar: str) -> dict:
    pass


def run_tests() -> None:
    s = scroll_link('text', 'vsb')
    assert s['widget'] == 'text'
    assert s['scrollbar'] == 'vsb'
    assert s['orient'] == 'vertical'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
