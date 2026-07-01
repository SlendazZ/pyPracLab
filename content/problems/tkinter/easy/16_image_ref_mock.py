# title: Image Reference Spec
# track: tkinter
# difficulty: easy
# tags: tkinter, image
# description: |
# Given path string, return image spec dict with path and keep_ref True (pattern for PhotoImage GC safety).
# examples:
# image_spec('/tmp/x.png') -> {'path':..., 'keep_ref': True}
# hint: |
# Plain dict; no actual image load.
# syntax_hint: |
# return {'path': path, 'keep_ref': True}


def image_spec(path: str) -> dict:
    pass


def run_tests() -> None:
    s = image_spec('/tmp/x.png')
    assert s['path'] == '/tmp/x.png'
    assert s['keep_ref'] is True
    assert image_spec('a.gif')['keep_ref'] is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
