def should_retry(code: int) -> bool:
    if code in (408, 429):
        return True
    return 500 <= code <= 599
