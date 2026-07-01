def sort_len(words: list[str]) -> list[str]:
    return sorted(words, key=lambda s: (len(s), s))
