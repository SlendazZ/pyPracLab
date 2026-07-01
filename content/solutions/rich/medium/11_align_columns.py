def format_row(cells: list[str], widths: list[int]) -> str:
    return ''.join(c.ljust(w) for c, w in zip(cells, widths))
