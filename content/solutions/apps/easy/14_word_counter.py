from collections import Counter

def count_words(sentence: str) -> dict[str, int]:
    words = sentence.lower().split()
    return dict(Counter(words))
