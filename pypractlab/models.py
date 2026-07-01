# Track and difficulty metadata.

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

DIFFICULTIES = ["easy", "medium", "hard"]

# slug, label, optional import guard
TRACK_SPECS: list[tuple[str, str, str | None]] = [
    ("algorithms", "Algorithms", None),
    ("syntax", "Python Syntax", None),
    ("automations", "Automations", None),
    ("apis", "APIs", None),
    ("servers", "Servers", None),
    ("apps", "Apps", None),
    ("fastapi", "FastAPI", "fastapi"),
    ("tkinter", "Tkinter", "tkinter"),
    ("requests", "Requests", "requests"),
    ("httpx", "HTTPX", "httpx"),
    ("pandas", "Pandas", "pandas"),
    ("rich", "Rich", "rich"),
    ("sqlite", "SQLite", "sqlite3"),
    ("bs4", "Beautiful Soup", "bs4"),
    ("click", "Click", "click"),
]

TRACK_ORDER: list[str] = [slug for slug, _, _ in TRACK_SPECS]
TRACK_LABELS: dict[str, str] = {slug: label for slug, label, _ in TRACK_SPECS}
TRACK_IMPORTS: dict[str, str | None] = {
    slug: imp for slug, _, imp in TRACK_SPECS
}


@dataclass(frozen=True)
class Problem:
    slug: str
    title: str
    track: str
    difficulty: str
    tags: tuple[str, ...]
    description: str
    examples: str
    hint: str
    syntax_hint: str
    path: Path
    rel_path: str
    solution_path: Path | None

    @property
    def has_solution(self) -> bool:
        return self.solution_path is not None and self.solution_path.exists()


@dataclass(frozen=True)
class Lesson:
    slug: str
    title: str
    track: str
    difficulty: str
    tags: tuple[str, ...]
    body: str
    path: Path
    rel_path: str
    exercise_rel_path: str | None


@dataclass
class Catalog:
    problems: list[Problem] = field(default_factory=list)
    lessons: list[Lesson] = field(default_factory=list)

    def problems_by_track(self, track: str) -> list[Problem]:
        return [p for p in self.problems if p.track == track]

    def lessons_by_track(self, track: str) -> list[Lesson]:
        return [l for l in self.lessons if l.track == track]

    @property
    def tracks_with_problems(self) -> list[str]:
        seen = {p.track for p in self.problems}
        return [t for t in TRACK_ORDER if t in seen]

    @property
    def tracks_with_lessons(self) -> list[str]:
        seen = {l.track for l in self.lessons}
        return [t for t in TRACK_ORDER if t in seen]
