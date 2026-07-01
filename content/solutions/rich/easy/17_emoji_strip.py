def strip_emoji(s: str) -> str:
    return ''.join(c for c in s if ord(c) < 0x10000)
