# title: Aligned Column Text
# track: rich
# difficulty: medium
# tags: rich
# description: |
# Given rows of strings, return one line with columns left-aligned in widths.
# examples:
# format_row(['a','bb'], [3,3]) -> 'a  bb '
# hint: |
# str.ljust for each cell.
# syntax_hint: |
# ''.join(cell.ljust(w) for cell, w in zip(cells, widths))


def format_row(cells: list[str], widths: list[int]) -> str:
    pass


def run_tests() -> None:
    assert format_row(['a', 'bb'], [3, 3]) == 'a  bb '
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
