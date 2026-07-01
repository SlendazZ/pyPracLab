def bearer_token(header: str) -> str | None:
    parts = header.split(None, 1)
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        return None
    return parts[1]
