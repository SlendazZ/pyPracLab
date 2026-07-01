def reverse_words(s: str) -> str:
    return ' '.join(w[::-1] for w in s.split())
