def segments(path: str) -> list[str]:
    return [s for s in path.split('/') if s]
