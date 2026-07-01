from collections import Counter

def top_words(words: list[str], n: int) -> list[tuple[str, int]]:
    return Counter(words).most_common(n)
