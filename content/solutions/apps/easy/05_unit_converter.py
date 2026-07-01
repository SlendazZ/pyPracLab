def convert(value: float, frm: str, to: str) -> float:
    factors = {'cm': 0.01, 'm': 1.0, 'km': 1000.0}
    base = value * factors[frm]
    return base / factors[to]
