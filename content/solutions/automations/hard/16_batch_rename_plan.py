from pathlib import Path

def plan(names: list[str], prefix: str) -> list[tuple[str, str]]:
    out = []
    width = max(3, len(str(len(names))))
    for i, name in enumerate(names, 1):
        ext = Path(name).suffix
        new = f"{prefix}_{i:0{width}d}{ext}"
        out.append((name, new))
    return out
