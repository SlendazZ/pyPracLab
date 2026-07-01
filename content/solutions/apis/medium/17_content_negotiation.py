def pick_type(accept: str, offered: list[str]) -> str | None:
    parts = [p.split(';')[0].strip() for p in accept.split(',')]
    for mime in parts:
        if mime in offered:
            return mime
    return None
