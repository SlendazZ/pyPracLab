def total_value(inv: dict) -> float:
    return sum(q * p for q, p in inv.values())
