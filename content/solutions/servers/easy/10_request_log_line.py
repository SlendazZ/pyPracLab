def log_line(method: str, path: str, status: int, size: int) -> str:
    return f"{method} {path} {status} {size}"
