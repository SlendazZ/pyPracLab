from rich.table import Table

def pair_table(name: str, value: str):
    table = Table()
    table.add_column('Name')
    table.add_column('Value')
    table.add_row(name, value)
    return table
