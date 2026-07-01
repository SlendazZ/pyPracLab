from collections import Counter

def can_build(note: str, mag: str) -> bool:
    return not (Counter(note) - Counter(mag))
