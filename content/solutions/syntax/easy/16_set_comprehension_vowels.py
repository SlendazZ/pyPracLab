def vowels(text: str) -> set[str]:
    return {ch for ch in text.lower() if ch in 'aeiou'}
