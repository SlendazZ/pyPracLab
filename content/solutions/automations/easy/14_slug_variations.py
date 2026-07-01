def slug_variants(title: str) -> tuple[str, str, str]:
    s = title.lower()
    return (s.replace(' ', '_'), s.replace(' ', '-'), s.replace(' ', '.'))
