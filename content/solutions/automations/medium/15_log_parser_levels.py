from collections import Counter

def count_levels(lines: list[str]) -> dict[str, int]:
    levels = {'ERROR', 'WARN', 'INFO'}
    c = Counter()
    for line in lines:
        parts = line.split()
        if len(parts) >= 2 and parts[1] in levels:
            c[parts[1]] += 1
    return dict(c)
