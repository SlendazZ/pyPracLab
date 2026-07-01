# title: Font Tuple Spec
# track: tkinter
# difficulty: easy
# tags: tkinter, font
# description: |
# Return Tk font spec tuple (family, size, style) for given family, size, and optional style.
# examples:
# font_tuple('Helvetica', 12, 'bold') -> ('Helvetica', 12, 'bold')
# hint: |
# Return 3-tuple; default style empty string.
# syntax_hint: |
# return (family, size, style or '')


def font_tuple(family: str, size: int, style: str = '') -> tuple:
    pass


def run_tests() -> None:
    assert font_tuple('Helvetica', 12, 'bold') == ('Helvetica', 12, 'bold')
    assert font_tuple('Arial', 10) == ('Arial', 10, '')
    assert font_tuple('Mono', 8, 'italic')[2] == 'italic'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
