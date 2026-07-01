def dir_size(d) -> int:
    from pathlib import Path
    p = Path(d)
    return sum(f.stat().st_size for f in p.rglob('*') if f.is_file())
