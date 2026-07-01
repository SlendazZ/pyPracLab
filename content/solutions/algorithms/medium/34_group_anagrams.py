from collections import defaultdict

def group(words: list[str]) -> list[list[str]]:
    buckets: dict = defaultdict(list)
    for w in words:
        buckets[tuple(sorted(w))].append(w)
    return list(buckets.values())
