def backup_plan(files: list, backup_dir) -> list[tuple]:
    from pathlib import Path
    bd = Path(backup_dir)
    return [(p, bd / (p.name + '.bak')) for p in files]
