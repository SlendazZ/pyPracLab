---
title: pathlib Essentials
track: automations
difficulty: easy
tags: pathlib, files
exercise: content/problems/automations/easy/10_extension_grouper.py
---

# pathlib Essentials

## Overview

Every automation script eventually touches the filesystem: reading configs, renaming photos, archiving logs, or organizing downloads. For years Python used string paths with `os.path.join` and `os.listdir`. `pathlib.Path` replaces that with a single object that knows how to join segments, test existence, read text, and walk directories — all with readable, chainable methods.

Think of a `Path` as an address label for a file or folder. You can inspect the label (`name`, `suffix`), check whether the place exists, and open it without converting back and forth between strings. If you are new to file automation, start here: pathlib is the modern default for any script that reads or writes files.

## Why pathlib instead of strings?

String paths work, but they are easy to get wrong:

```python
# Old style — easy to mix separators or forget edge cases
import os
folder = os.path.join('output', 'reports', '2026')
for name in os.listdir(folder):
    full = os.path.join(folder, name)
```

The pathlib version reads top to bottom like a sentence:

```python
from pathlib import Path

folder = Path('output') / 'reports' / '2026'
for path in folder.iterdir():
    print(path.name)
```

Same result, fewer moving parts, and `path` is already a `Path` object — no re-wrapping on every loop iteration.

## Creating paths

Start by importing `Path` and building locations from strings or other paths:

```python
from pathlib import Path

root = Path('.')                          # current directory
readme = Path('docs/readme.md')           # relative path
config = Path.home() / '.config' / 'myapp' / 'settings.json'
```

The `/` operator joins segments. Python picks `/` on Linux and macOS, `\` on Windows — you never hard-code separators. `Path.home()` expands to the user's home directory (`/home/you` or `C:\Users\you`).

Build paths step by step when a script receives parts from different places:

```python
base = Path('/var/log')
app_name = 'myapp'
log_file = base / app_name / 'app.log'
# Path('/var/log/myapp/app.log')
```

Convert legacy APIs that expect strings with `str(p)` or `os.fspath(p)`:

```python
import subprocess
subprocess.run(['ls', str(root)], check=True)
```

## Inspecting paths

Path objects expose the pieces of a filepath as attributes. This is faster and clearer than splitting strings yourself:

```python
p = Path('docs/readme.md')
p.name       # 'readme.md'   — filename with extension
p.stem       # 'readme'      — filename without extension
p.suffix     # '.md'         — extension including the dot
p.parent     # Path('docs')  — containing folder
p.parts      # ('docs', 'readme.md')
```

Walk through a real rename scenario. You have `photo.JPG` and want a lowercase extension plus a dated backup name:

```python
original = Path('downloads/photo.JPG')
normalized = original.with_suffix('.jpg')
backup = original.with_name(f'{original.stem}_2026-07-01{original.suffix}')
# Path('downloads/photo_2026-07-01.JPG')
```

Useful variations when building output names:

```python
backup = p.with_suffix('.bak')       # Path('docs/readme.bak')
copy = p.with_name('readme_copy.md') # Path('docs/readme_copy.md')
```

## Existence and type checks

Before reading or writing, confirm the path points where you expect:

```python
p = Path('docs/readme.md')
p.exists()     # True if anything is at this path
p.is_file()    # True only for regular files
p.is_dir()     # True only for directories
p.resolve()    # absolute path, symlinks followed
```

A safe read pattern checks first and gives a clear error:

```python
def read_config(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f'config not found: {path}')
    return path.read_text(encoding='utf-8')
```

Create missing directories safely before writing output:

```python
out_dir = Path('output/reports')
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / 'summary.txt').write_text('done\n', encoding='utf-8')
```

`parents=True` creates intermediate folders; `exist_ok=True` avoids errors when the folder already exists.

## Reading and writing

For small text files, pathlib shortcuts replace manual `open`/`close`:

```python
p = Path('notes.txt')
text = p.read_text(encoding='utf-8')
p.write_text('hello\n', encoding='utf-8')
raw = p.read_bytes()   # for images, PDFs, etc.
```

Always pass `encoding='utf-8'` on text files — especially on Windows, where the default encoding may not be UTF-8.

Worked example: append a timestamped line to a log file:

```python
from datetime import datetime, timezone

log = Path('logs/app.log')
log.parent.mkdir(parents=True, exist_ok=True)
stamp = datetime.now(timezone.utc).isoformat()
with log.open('a', encoding='utf-8') as f:
    f.write(f'{stamp} backup complete\n')
```

Step by step:
1. `log.parent.mkdir` ensures the `logs/` folder exists.
2. Open in append mode (`'a'`) so previous lines stay.
3. Write one line with a newline at the end.

For large files or line-by-line processing, combine `Path` with `open`:

```python
with p.open(encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())
```

## Walking directories

List one directory or search recursively:

```python
folder = Path('src')
for child in folder.iterdir():
    print(child.name)

for path in folder.glob('*.py'):      # this folder only
    print(path)

for path in folder.rglob('*.py'):     # all subfolders too
    print(path.relative_to(folder))
```

`glob` matches a pattern in one directory; `rglob` walks the whole tree. Use `relative_to(root)` when you want paths without a long prefix.

Find every `.log` file modified in the last 7 days:

```python
import time

cutoff = time.time() - 7 * 24 * 3600
for path in Path('/var/log').rglob('*.log'):
    if path.is_file() and path.stat().st_mtime >= cutoff:
        print(path, path.stat().st_size, 'bytes')
```

`stat()` returns metadata: size, modification time, permissions. Handy for cleanup scripts that delete old files.

## Worked example: group files by extension

Here is a complete script that scans a folder and groups filenames by extension — the pattern behind the practice exercise:

```python
from pathlib import Path
from collections import defaultdict

def group_by_extension(folder: Path) -> dict[str, list[Path]]:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in folder.iterdir():
        if path.is_file():
            ext = path.suffix.lower() or '(no extension)'
            groups[ext].append(path)
    return dict(groups)

downloads = Path.home() / 'Downloads'
for ext, files in sorted(group_by_extension(downloads).items()):
    print(f'{ext}: {len(files)} file(s)')
```

Step by step:
1. `iterdir()` yields every entry in the folder.
2. `is_file()` skips subdirectories.
3. `suffix` gives `.jpg`, `.pdf`, etc.; empty string means no extension.
4. `defaultdict(list)` appends without checking if the key exists yet.
5. `sorted(...)` prints extensions in alphabetical order.

Extend it: move each group into its own subfolder:

```python
def organize_by_extension(folder: Path) -> None:
    for ext, files in group_by_extension(folder).items():
        target = folder / ext.lstrip('.')
        target.mkdir(exist_ok=True)
        for path in files:
            path.rename(target / path.name)
```

A rename helper built from the same pieces:

```python
def backup_path(original: Path) -> Path:
    return original.with_name(f'{original.stem}_backup{original.suffix}')
```

## Common automation patterns

- Group files by extension for batch rename or organize
- Find duplicate sizes or names under a tree with `rglob` + a dict
- Build output paths with `dest = out_dir / f'{stem}_copy{p.suffix}'`
- Filter by date with `path.stat().st_mtime` for cleanup scripts
- Mirror a folder tree with `relative_to` and `mkdir(parents=True)`

## Common pitfalls

- Mixing `str` and `Path` — convert with `Path(s)` or `str(p)` for legacy APIs
- Forgetting encoding on text files on Windows
- Using `glob('*')` when you need recursion (`rglob`)
- Calling `iterdir()` on a file path — it raises; check `is_dir()` first
- Assuming `exists()` means readable — permissions still matter
- `rename` across filesystems may fail — use `shutil.move` for cross-device moves

## Practice

Group files in a directory by extension using pathlib.

## Summary

Path objects are immutable values. Prefer them over raw strings for any script that touches the filesystem. Join with `/`, inspect with `.name` and .suffix`, walk with `rglob`, and always set `encoding='utf-8'` for text.
