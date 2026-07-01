from pathlib import Path
from collections import defaultdict

def group_ext(names: list[str]) -> dict[str, list[str]]:
    d: dict[str, list[str]] = defaultdict(list)
    for n in names:
        d[Path(n).suffix.lstrip('.')].append(n)
    return dict(d)
