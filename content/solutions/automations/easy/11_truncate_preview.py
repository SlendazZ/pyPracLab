def preview(text: str, n: int) -> str:
    s = ' '.join(text.split())
    if len(s) <= n:
        return s
    return s[:max(0, n - 3)] + '...'
