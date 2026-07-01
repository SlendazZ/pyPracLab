def status_line(code: int, reason: str) -> str:
    return f"HTTP/1.1 {code} {reason}"
