def price_table(rows: list[tuple[str, float]]) -> list[str]:
    return [f'{name}: ${price:.2f}' for name, price in rows]
