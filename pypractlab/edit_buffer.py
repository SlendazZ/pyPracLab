# Staging problem files for edit without revealing hidden hints.

from __future__ import annotations

from pathlib import Path

from .catalog import ROOT, _HEADER_RE

EDIT_DIR = ROOT / ".practice" / "editing"


def staging_path(problem_path: Path) -> Path:
    rel = problem_path.relative_to(ROOT)
    return EDIT_DIR / rel


def header_end_index(text: str) -> int:
    pos = 0
    for raw in text.splitlines(keepends=True):
        if not raw.strip():
            pos += len(raw)
            continue
        if not raw.lstrip().startswith("#"):
            return pos
        pos += len(raw)
    return pos


def omit_header_fields(text: str, omit: frozenset[str]) -> str:
    if not omit:
        return text
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        stripped = raw.rstrip("\n\r")
        if not stripped.strip():
            out.append(raw)
            i += 1
            continue
        if not stripped.lstrip().startswith("#"):
            out.extend(lines[i:])
            break
        m = _HEADER_RE.match(stripped.lstrip())
        if m and m.group(1).lower() in omit:
            value = m.group(2)
            i += 1
            if value.rstrip() == "|" or value == "":
                while i < n:
                    s = lines[i].rstrip("\n\r")
                    if not s.strip():
                        i += 1
                        continue
                    if not s.lstrip().startswith("#"):
                        break
                    if _HEADER_RE.match(s.lstrip()):
                        break
                    i += 1
            continue
        out.append(raw)
        i += 1
    return "".join(out)


def merge_staged_into_original(problem_path: Path) -> bool:
    staged = staging_path(problem_path)
    if not staged.is_file():
        return False
    original = problem_path.read_text(encoding="utf-8")
    edited = staged.read_text(encoding="utf-8")
    h = header_end_index(original)
    c = header_end_index(edited)
    problem_path.write_text(original[:h] + edited[c:], encoding="utf-8")
    staged.unlink(missing_ok=True)
    return True


def prepare_problem_for_edit(
    problem_path: Path,
    *,
    show_hint: bool,
    show_syntax: bool,
) -> tuple[Path, Path | None]:
    merge_staged_into_original(problem_path)

    omit: set[str] = set()
    if not show_hint:
        omit.add("hint")
    if not show_syntax:
        omit.add("syntax_hint")
    if not omit:
        return problem_path, None

    text = problem_path.read_text(encoding="utf-8")
    stripped = omit_header_fields(text, frozenset(omit))
    dest = staging_path(problem_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(stripped, encoding="utf-8")
    return dest, problem_path
