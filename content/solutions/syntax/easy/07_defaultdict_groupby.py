from collections import defaultdict

def group_by_len(words: list[str]) -> dict[int, list[str]]:
    d: dict[int, list[str]] = defaultdict(list)
    for w in words:
        d[len(w)].append(w)
    return dict(d)
