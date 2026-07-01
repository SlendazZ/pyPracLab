# Discover and parse problems and lessons from content/.

from __future__ import annotations

import re
from pathlib import Path

from .models import (
    DIFFICULTIES,
    Catalog,
    Lesson,
    Problem,
    TRACK_IMPORTS,
)

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PROBLEMS_DIR = CONTENT / "problems"
SOLUTIONS_DIR = CONTENT / "solutions"
LESSONS_DIR = CONTENT / "lessons"

_HEADER_RE = re.compile(r"^#\s*([A-Za-z_][\w-]*)\s*:\s?(.*)$")
_HEADER_KEYS = frozenset({
    "title", "track", "difficulty", "tags", "description",
    "examples", "hint", "syntax_hint",
})


def _dedent_block(lines: list[str]) -> str:
    non_empty = [ln for ln in lines if ln.strip()]
    if not non_empty:
        return ""
    common = min(len(ln) - len(ln.lstrip(" ")) for ln in non_empty)
    stripped = [ln[common:] if ln.strip() else "" for ln in lines]
    return "\n".join(stripped).strip("\n")


def _parse_block_header(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []
    is_block = False

    def flush() -> None:
        nonlocal current_key, current_lines, is_block
        if current_key is not None:
            if is_block:
                fields[current_key] = _dedent_block(current_lines)
            else:
                fields[current_key] = "\n".join(current_lines).strip()
        current_key = None
        current_lines = []
        is_block = False

    for raw in text.splitlines():
        if not raw.strip():
            if current_key is not None and is_block:
                current_lines.append("")
            continue
        if not raw.startswith("#"):
            break
        m = _HEADER_RE.match(raw)
        if m:
            key = m.group(1).lower()
            value = m.group(2)
            if is_block and key not in _HEADER_KEYS:
                stripped = raw[1:]
                if stripped.startswith(" "):
                    stripped = stripped[1:]
                current_lines.append(stripped)
                continue
            flush()
            if value.rstrip() == "|" or value == "":
                current_key = key
                is_block = True
                current_lines = []
            else:
                current_key = key
                is_block = False
                current_lines = [value]
            continue
        if current_key is not None and is_block:
            stripped = raw[1:]
            if stripped.startswith(" "):
                stripped = stripped[1:]
            current_lines.append(stripped)
            continue
        continue

    flush()
    return fields


def _split_tags(raw: str) -> tuple[str, ...]:
    return tuple(t.strip() for t in raw.split(",") if t.strip())


def _difficulty_from_path(path: Path) -> str | None:
    parts = path.relative_to(PROBLEMS_DIR).parts
    if len(parts) >= 2 and parts[1] in DIFFICULTIES:
        return parts[1]
    return None


def _track_from_path(path: Path, base: Path) -> str | None:
    parts = path.relative_to(base).parts
    return parts[0] if parts else None


def _solution_for(problem_path: Path) -> Path | None:
    rel = problem_path.relative_to(PROBLEMS_DIR)
    return SOLUTIONS_DIR / rel


def discover_problems() -> list[Problem]:
    problems: list[Problem] = []
    if not PROBLEMS_DIR.exists():
        return problems
    for path in sorted(PROBLEMS_DIR.rglob("*.py")):
        if path.name.startswith("__"):
            continue
        text = path.read_text(encoding="utf-8")
        header = _parse_block_header(text)
        title = header.get("title", "").strip()
        if not title:
            continue
        track = header.get("track", "").strip() or _track_from_path(path, PROBLEMS_DIR) or ""
        difficulty = header.get("difficulty", "").strip().lower()
        if difficulty not in DIFFICULTIES:
            difficulty = _difficulty_from_path(path) or "medium"
        tags = _split_tags(header.get("tags", ""))
        sol = _solution_for(path)
        rel = path.relative_to(ROOT).as_posix()
        problems.append(
            Problem(
                slug=path.stem,
                title=title,
                track=track,
                difficulty=difficulty,
                tags=tags,
                description=header.get("description", "").strip(),
                examples=header.get("examples", "").strip(),
                hint=header.get("hint", "").strip(),
                syntax_hint=header.get("syntax_hint", "").strip(),
                path=path,
                rel_path=rel,
                solution_path=sol,
            )
        )
    return problems


def _parse_lesson_frontmatter(text: str) -> tuple[dict[str, str], str]:
    fields: dict[str, str] = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fields, text.strip("\n")
    body_start = 1
    fm: list[str] = []
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            body_start = i + 1
            break
        fm.append(lines[i])
    current_key: str | None = None
    current_lines: list[str] = []
    for raw in fm:
        if raw.startswith(" ") and current_key is not None:
            current_lines.append(raw.strip())
            continue
        if ":" in raw:
            if current_key is not None:
                fields[current_key] = "\n".join(current_lines).strip()
            key, _, value = raw.partition(":")
            current_key = key.strip().lower()
            current_lines = [value.strip()]
    if current_key is not None:
        fields[current_key] = "\n".join(current_lines).strip()
    body = "\n".join(lines[body_start:]).strip("\n")
    return fields, body


def discover_lessons() -> list[Lesson]:
    lessons: list[Lesson] = []
    if not LESSONS_DIR.exists():
        return lessons
    for path in sorted(LESSONS_DIR.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        fields, body = _parse_lesson_frontmatter(text)
        title = fields.get("title", "").strip()
        if not title:
            continue
        track = fields.get("track", "").strip() or _track_from_path(path, LESSONS_DIR) or ""
        difficulty = fields.get("difficulty", "").strip().lower()
        if difficulty not in DIFFICULTIES:
            difficulty = "medium"
        tags = _split_tags(fields.get("tags", ""))
        exercise = fields.get("exercise", "").strip() or None
        rel = path.relative_to(ROOT).as_posix()
        lessons.append(
            Lesson(
                slug=path.stem,
                title=title,
                track=track,
                difficulty=difficulty,
                tags=tags,
                body=body,
                path=path,
                rel_path=rel,
                exercise_rel_path=exercise,
            )
        )
    return lessons


def load_catalog() -> Catalog:
    return Catalog(problems=discover_problems(), lessons=discover_lessons())


def lib_available(track: str) -> bool:
    imp = TRACK_IMPORTS.get(track)
    if imp is None:
        return True
    try:
        __import__(imp)
        return True
    except Exception:
        return False
