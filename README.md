# pyPracLab

A keyboard-driven terminal app for practicing Python: 350+ problems and 34
lessons across the standard library and common packages, rated easy /
medium / hard.

<img width="1912" height="1161" alt="problems" src="https://github.com/user-attachments/assets/cb10e728-3493-4005-ad42-ee113e172dff" />
<img width="1912" height="1161" alt="lesson" src="https://github.com/user-attachments/assets/34014cd5-bc96-454b-98b6-c940183d402a" />



## Quickstart

Requires Python 3.10+.

```bash
./run.sh          # Linux / macOS — sets up .venv on first run
.\run.ps1         # Windows (PowerShell) — same, plus windows-curses
```

Or:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pypractlab
```

Other flags: `--check` (verify all problems), `--run <path>` (run one problem's tests).

Navigation: arrows to move, `enter` to open, `esc`/`b` back, `1`/`2`/`3` for
Problems/Lessons/Settings, `f` to favorite, `?` for the full key list.

## Adding problems

Problems are generated from spec dicts, not written by hand one at a time.

1. Add a dict to a track file under `tools/specs/` with `slug`, `track`,
  `difficulty`, `title`, `tags`, `description`, `signature`, `tests`, and
   `solution` (optionally `hint`, `syntax_hint`, `examples`).
2. New track? Register it in `tools/specs/__init__.py` and
  `pypractlab/models.py`.
3. Generate:
  ```bash
   python tools/gen_content.py            # write missing files only
   python tools/gen_content.py --force    # overwrite existing files
   python tools/gen_content.py --check    # generate + verify solutions
  ```
4. Confirm with `./run.sh --check`.

Lessons work the same way, specs live in `tools/specs/lesson_guides/`.

NOTE: /content is mostly ai-generated
