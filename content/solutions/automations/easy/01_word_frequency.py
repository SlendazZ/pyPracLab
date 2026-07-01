from collections import Counter

def word_counts(text: str) -> dict[str, int]:
    return dict(Counter(text.lower().split()))
