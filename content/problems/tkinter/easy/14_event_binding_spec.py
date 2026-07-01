# title: Event Binding Spec
# track: tkinter
# difficulty: easy
# tags: tkinter, events
# description: |
# Given widget name and event sequence (e.g. '<Button-1>'), return binding spec dict.
# examples:
# bind_spec('btn', '<Button-1>', 'on_click') -> binding dict
# hint: |
# Dict with widget, sequence, handler keys.
# syntax_hint: |
# return {'widget': w, 'sequence': seq, 'handler': handler}


def bind_spec(widget: str, sequence: str, handler: str) -> dict:
    pass


def run_tests() -> None:
    assert bind_spec('btn', '<Button-1>', 'on_click') == {
        'widget': 'btn', 'sequence': '<Button-1>', 'handler': 'on_click'}
    assert bind_spec('x', '<Key>', 'h')['sequence'] == '<Key>'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
