def rotate_lines(text: str, k: int) -> str:
    if not text:
        return ''
    lines = text.splitlines()
    if not lines:
        return ''
    k %= len(lines)
    return '\n'.join(lines[k:] + lines[:k])
