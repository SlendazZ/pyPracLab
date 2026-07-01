from collections import Counter

def dup_lines(text: str) -> set[str]:
    counts = Counter(text.splitlines())
    return {line for line, c in counts.items() if c > 1}
