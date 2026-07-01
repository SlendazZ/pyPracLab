def count_errors(text: str) -> int:
    return sum('ERROR' in line for line in text.splitlines())
