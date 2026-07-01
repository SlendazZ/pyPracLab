from pathlib import Path

def path_parts(p: str) -> tuple[str, str, str]:
    path = Path(p)
    return str(path.parent), path.name, path.suffix
