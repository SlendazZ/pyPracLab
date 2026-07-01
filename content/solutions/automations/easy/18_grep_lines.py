def grep_lines(text: str, needle: str) -> list[str]:
    return [ln for ln in text.splitlines() if needle in ln]
