def temp(value: float, frm: str, to: str) -> float:
    if frm == 'C':
        c = value
    elif frm == 'F':
        c = (value - 32) * 5 / 9
    else:
        c = value - 273.15
    if to == 'C':
        return c
    if to == 'F':
        return c * 9 / 5 + 32
    return c + 273.15
