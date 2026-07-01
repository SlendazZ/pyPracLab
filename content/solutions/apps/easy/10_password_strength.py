def strength(p: str) -> str:
    if len(p) < 8:
        return 'weak'
    has_upper = any(c.isupper() for c in p)
    has_digit = any(c.isdigit() for c in p)
    if has_upper and has_digit:
        return 'strong'
    return 'medium'
