from rich.table import Table

def build_table(headers: list[str], rows: list[tuple]) -> Table:
    table = Table()
    for h in headers:
        table.add_column(h)
    for row in rows:
        table.add_row(*row)
    return table
