# Application state and keyboard input (testable without curses).

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from ..catalog import load_catalog
from ..edit_buffer import merge_staged_into_original, prepare_problem_for_edit
from ..editor import _editor_command, open_window
from ..models import DIFFICULTIES, Catalog, Lesson, Problem, TRACK_LABELS
from ..runner import run_problem
from ..settings import (
    EDITOR_CANDIDATES,
    OPEN_MODES,
    SORT_MODES,
    TERMINAL_CANDIDATES,
    Settings,
    load_favorites,
    load_progress,
    save_favorites,
    save_progress,
)
from ..themes import THEME_NAMES, cycle_theme, normalize_theme, shuffle_theme
from .keys import KEY_DOWN, KEY_ENTER, KEY_ESC, KEY_PAGE_DOWN, KEY_PAGE_UP, KEY_UP
from .snowfall import Snowfall

SORT_LABELS = {"name": "A-Z", "completion": "status", "difficulty": "difficulty", "number": "number"}
DIFF_FILTERS = ["all", "easy", "medium", "hard"]
FAVORITES_TRACK = "__favorites__"

MAIN_ITEMS = [
    ("problems", "Problems"),
    ("lessons", "Lessons"),
    ("settings", "Settings"),
    ("quit", "Quit"),
]

SETTINGS_FIELDS = [
    ("editor", "Editor", "editor"),
    ("open_mode", "Editor open mode", "open_mode"),
    ("terminal", "Terminal (new window)", "terminal"),
    ("theme", "Theme", "theme"),
    ("default_sort", "Default sort", "default_sort"),
    ("default_difficulty_filter", "Default difficulty filter", "diff"),
    ("show_hints_default", "Show hints by default", "bool"),
    ("show_syntax_hints_default", "Show syntax hints by default", "bool"),
    ("snowfall_enabled", "Snowfall", "bool"),
]


@dataclass
class ScreenState:
    name: str
    data: dict = field(default_factory=dict)


@dataclass
class ListRow:
    key: str
    label: str
    detail: str = ""
    done: bool = False
    favorite: bool = False


class AppController:
    """Holds navigation state and handles keyboard input."""

    def __init__(self) -> None:
        self.catalog: Catalog = load_catalog()
        self.settings: Settings = Settings.load()
        self.settings.validate()
        self.progress: dict[str, str] = load_progress()
        self.favorites: dict[str, str] = load_favorites()
        self.stack: list[ScreenState] = [ScreenState("main")]
        self.index: int = 0
        self.scroll: int = 0
        self._saved_index: dict[str, int] = {}
        self.output: str = ""
        self.show_hint: bool = self.settings.show_hints_default
        self.show_syntax: bool = self.settings.show_syntax_hints_default
        self.sort: str = self.settings.default_sort
        self.diff_filter: str = self.settings.default_difficulty_filter
        self.lesson_mode: str = "tracks"
        self.lesson_track: str | None = None
        self.quit_requested: bool = False
        self.frame: int = 0
        self.snow = Snowfall()
        self._snow_size: tuple[int, int] = (0, 0)
        self.needs_suspend: Path | None = None
        self.suspend_message: str = ""
        self.edit_merge_target: Path | None = None

    def is_done(self, rel_path: str) -> bool:
        return rel_path in self.progress

    def is_favorite(self, rel_path: str) -> bool:
        return rel_path in self.favorites

    def toggle_favorite(self, rel_path: str) -> bool:
        """Toggle favorite; returns True if now favorited."""
        if rel_path in self.favorites:
            del self.favorites[rel_path]
            save_favorites(self.favorites)
            return False
        self.favorites[rel_path] = datetime.now(timezone.utc).isoformat()
        save_favorites(self.favorites)
        return True

    def mark_done(self, rel_path: str) -> None:
        self.progress[rel_path] = datetime.now(timezone.utc).isoformat()
        save_progress(self.progress)

    def save_settings(self) -> None:
        self.settings.theme = normalize_theme(self.settings.theme)
        self.settings.validate()
        self.settings.save()

    def progress_summary(self) -> str:
        total = len(self.catalog.problems)
        done = sum(1 for p in self.catalog.problems if p.rel_path in self.progress)
        pct = (done * 100 // total) if total else 0
        return f"{done}/{total} ({pct}%)"

    @property
    def screen(self) -> ScreenState:
        return self.stack[-1]

    def _list_identity(self) -> str:
        """Stable key for the current list view, used to remember the last
        selected item across navigation. Empty string means don't remember."""
        s = self.screen
        if s.name == "main":
            return "main"
        if s.name == "problems_tracks":
            return "problems_tracks"
        if s.name == "problems_list":
            return f"problems_list:{s.data.get('track')}"
        if s.name == "lessons":
            if self.lesson_mode == "tracks":
                return "lessons_tracks"
            return f"lessons_list:{self.lesson_track}"
        if s.name == "settings":
            return "settings"
        return ""

    def _remember_index(self) -> None:
        key = self._list_identity()
        if key:
            self._saved_index[key] = self.index

    def _recall_index(self, default: int = 0) -> None:
        key = self._list_identity()
        idx = self._saved_index.get(key, default) if key else default
        rows = self.list_rows()
        self.index = max(0, min(idx, len(rows) - 1)) if rows else 0

    def push(self, name: str, *, default_index: int = 0, **data: object) -> None:
        self._remember_index()
        self.stack.append(ScreenState(name, dict(data)))
        self.scroll = 0
        self.output = ""
        self._recall_index(default=default_index)

    def pop(self) -> None:
        if len(self.stack) > 1:
            leaving = self.screen
            if leaving.name == "problem_detail":
                p: Problem = leaving.data["problem"]
                merge_staged_into_original(p.path)
                self.edit_merge_target = None
            self._remember_index()
            self.stack.pop()
            self.index = 0
            self.scroll = 0
            self.output = ""
            self._recall_index()

    def _action_back(self) -> bool:
        """Go back one level. Returns True if navigation changed."""
        s = self.screen
        if s.name == "main":
            return False
        if s.name == "lessons" and self.lesson_mode == "lessons":
            self._remember_index()
            self.lesson_mode = "tracks"
            self.lesson_track = None
            self.index = 0
            self.scroll = 0
            self._recall_index()
            return True
        if len(self.stack) > 1:
            self.pop()
            return True
        return False

    def header_left(self) -> str:
        s = self.screen
        if s.name == "main":
            return "menu"
        if s.name == "problems_tracks":
            return "problems"
        if s.name == "problems_list":
            track = str(s.data["track"])
            if track == FAVORITES_TRACK:
                return "problems > favorites"
            return f"problems > {track}"
        if s.name == "problem_detail":
            p: Problem = s.data["problem"]
            return f"problems > {p.track} > {p.slug}"
        if s.name == "lessons":
            if self.lesson_mode == "tracks":
                return "lessons"
            return f"lessons > {TRACK_LABELS.get(self.lesson_track or '', self.lesson_track or '')}"
        if s.name == "lesson_reader":
            l: Lesson = s.data["lesson"]
            return f"lessons > {l.track} > {l.slug}"
        if s.name == "settings":
            return "settings"
        if s.name == "help":
            return "help"
        return "pyPracLab"

    def footer_hints(self) -> list[tuple[str, str]]:
        s = self.screen
        if s.name == "main":
            return [("↑↓", "move"), ("enter", "select"), ("1-3", "jump"), ("?", "help"), ("t", "theme"), ("q", "quit")]
        if s.name in ("problems_tracks", "lessons"):
            return [("↑↓", "move"), ("enter", "open"), ("esc/b", "back")]
        if s.name == "settings":
            return [("↑↓", "move"), ("enter", "cycle"), ("esc/b", "back")]
        if s.name == "problems_list":
            return [
                ("↑↓", "move"),
                ("enter", "open"),
                ("f", "favorite"),
                ("s", f"sort:{SORT_LABELS[self.sort]}"),
                ("0-3", "filter"),
                ("esc/b", "back"),
            ]
        if s.name == "problem_detail":
            return [
                ("e", "edit"),
                ("r", "run"),
                ("h", "hint"),
                ("y", "syntax hint"),
                ("f", "favorite"),
                ("esc/b", "back"),
            ]
        if s.name == "lesson_reader":
            hints = [("esc/b", "back"), ("↑↓", "scroll")]
            l: Lesson = s.data["lesson"]
            if l.exercise_rel_path:
                hints.insert(0, ("e", "exercise"))
            return hints
        if s.name == "help":
            return [("esc/b", "back")]
        return []

    def list_rows(self) -> list[ListRow]:
        s = self.screen
        if s.name == "main":
            return [
                ListRow(k, label, detail=self._main_menu_preview(k))
                for k, label in MAIN_ITEMS
            ]
        if s.name == "problems_tracks":
            rows: list[ListRow] = []
            rows.append(
                ListRow(
                    FAVORITES_TRACK,
                    "Favorites",
                    str(len(self.favorites)),
                    favorite=True,
                )
            )
            for track in self.catalog.tracks_with_problems:
                items = self.catalog.problems_by_track(track)
                done = sum(1 for p in items if p.rel_path in self.progress)
                label = TRACK_LABELS.get(track, track)
                rows.append(ListRow(track, label, f"{done}/{len(items)}"))
            return rows
        if s.name == "problems_list":
            track = str(s.data["track"])
            problems = self._sorted_filtered(track)
            s.data["problems"] = problems
            rows = []
            for p in problems:
                solved = self.is_done(p.rel_path)
                favorited = self.is_favorite(p.rel_path)
                mark = "done" if solved else p.difficulty
                if favorited:
                    mark = f"fav  {mark}"
                rows.append(
                    ListRow(p.rel_path, p.title, mark, done=solved, favorite=favorited)
                )
            return rows
        if s.name == "lessons":
            if self.lesson_mode == "tracks":
                rows = []
                for track in self.catalog.tracks_with_lessons:
                    count = self.catalog.lessons_by_track(track)
                    label = TRACK_LABELS.get(track, track)
                    rows.append(ListRow(f"track:{track}", label, str(len(count))))
                return rows
            lessons = self.catalog.lessons_by_track(self.lesson_track or "")
            s.data["lessons"] = lessons
            return [
                ListRow(
                    l.rel_path,
                    l.title,
                    f"{'r' if self.is_done(l.rel_path) else '.'} {l.difficulty}",
                )
                for l in lessons
            ]
        if s.name == "settings":
            return [
                ListRow(attr, label, str(getattr(self.settings, attr)))
                for attr, label, _ in SETTINGS_FIELDS
            ]
        return []

    def _preview_line(self, names: list[str], *, limit: int = 3) -> str:
        if not names:
            return "(empty)"
        parts = names[:limit]
        line = " · ".join(parts)
        if len(names) > limit:
            line += " · ..."
        return line

    def _main_menu_preview(self, key: str) -> str:
        if key == "problems":
            names = [
                TRACK_LABELS.get(t, t) for t in self.catalog.tracks_with_problems
            ]
            return self._preview_line(names)
        if key == "lessons":
            names = [
                TRACK_LABELS.get(t, t) for t in self.catalog.tracks_with_lessons
            ]
            return self._preview_line(names)
        if key == "settings":
            names = [label for _, label, _ in SETTINGS_FIELDS]
            return self._preview_line(names)
        return ""

    def _favorite_problems(self) -> list[Problem]:
        by_path = {p.rel_path: p for p in self.catalog.problems}
        return [by_path[rel] for rel in self.favorites if rel in by_path]

    def _sorted_filtered(self, track: str) -> list[Problem]:
        if track == FAVORITES_TRACK:
            items = self._favorite_problems()
        else:
            items = list(self.catalog.problems_by_track(track))
        if self.diff_filter != "all":
            items = [p for p in items if p.difficulty == self.diff_filter]
        if self.sort == "name":
            items.sort(key=lambda p: p.title.lower())
        elif self.sort == "completion":
            items.sort(key=lambda p: (p.rel_path in self.progress, p.title.lower()))
        elif self.sort == "difficulty":
            items.sort(key=lambda p: (DIFFICULTIES.index(p.difficulty), p.slug))
        else:
            items.sort(key=lambda p: p.slug)
        return items

    def breadcrumb(self) -> str:
        s = self.screen
        if s.name == "problems_tracks":
            return "pick a track"
        if s.name == "problems_list":
            track = str(s.data["track"])
            if track == FAVORITES_TRACK:
                label = "Favorites"
            else:
                label = TRACK_LABELS.get(track, track)
            filt = "" if self.diff_filter == "all" else f"  [{self.diff_filter}]"
            srt = SORT_LABELS[self.sort]
            return f"{label}   sort:{srt}{filt}"
        if s.name == "lessons":
            if self.lesson_mode == "tracks":
                return "pick a track"
            label = TRACK_LABELS.get(self.lesson_track or "", self.lesson_track or "")
            return label
        if s.name == "settings":
            return "enter to cycle a value"
        if s.name == "main":
            return ""
        return ""

    def selected_problem(self) -> Problem | None:
        if self.screen.name != "problems_list":
            return None
        rows = self.list_rows()
        self.clamp_index(rows)
        if not rows:
            return None
        rel = rows[self.index].key
        for p in self.screen.data.get("problems", []):
            if p.rel_path == rel:
                return p
        return None

    def problem_list_preview_lines(self) -> list[tuple[str, str]]:
        """Compact preview for the problems list selection."""
        p = self.selected_problem()
        if p is None:
            return []
        done = "done" if self.is_done(p.rel_path) else "todo"
        meta = f"{p.difficulty}  |  {done}"
        if self.is_favorite(p.rel_path):
            meta += "  |  favorite"
        if p.tags:
            meta += f"  |  {', '.join(p.tags)}"
        lines: list[tuple[str, str]] = [
            ("muted", meta),
            ("normal", p.description.strip() or "(no description)"),
        ]
        if p.examples:
            first = p.examples.strip().splitlines()[0]
            lines.append(("muted", f"e.g. {first}"))
        return lines

    def problem_detail_lines(self) -> list[tuple[str, str]]:
        """Return (style, text) lines for problem detail view."""
        p: Problem = self.screen.data["problem"]
        lines: list[tuple[str, str]] = []
        done = "done" if self.is_done(p.rel_path) else "todo"
        fav = "favorite" if self.is_favorite(p.rel_path) else ""
        title_bits = [p.title, p.difficulty, done]
        if fav:
            title_bits.append(fav)
        lines.append(("title", "  |  ".join(title_bits)))
        if p.tags:
            lines.append(("muted", f"tags: {', '.join(p.tags)}"))
        lines.append(("normal", ""))
        lines.append(("normal", p.description or "(no description)"))
        if p.examples:
            lines.append(("normal", ""))
            lines.append(("muted", "examples:"))
            lines.append(("normal", p.examples))
        if self.show_hint and p.hint:
            lines.append(("normal", ""))
            lines.append(("hint", "hint:"))
            lines.append(("hint", p.hint))
        if self.show_syntax and p.syntax_hint:
            lines.append(("normal", ""))
            lines.append(("syntax", "syntax hint:"))
            lines.append(("syntax", p.syntax_hint))
        if self.output:
            lines.append(("normal", ""))
            lines.append(("output", "--- output ---"))
            for ln in self.output.splitlines():
                lines.append(("output", ln))
        return lines

    def lesson_reader_lines(self) -> list[tuple[str, str]]:
        l: Lesson = self.screen.data["lesson"]
        lines: list[tuple[str, str]] = [
            ("title", f"{l.title}  |  {l.difficulty}"),
            ("normal", ""),
        ]
        for raw in (l.body or "(empty lesson)").splitlines():
            style = "normal"
            if raw.startswith("# "):
                style = "title"
                raw = raw[2:]
            elif raw.startswith("## "):
                style = "primary"
                raw = raw[3:]
            elif raw.startswith("### "):
                style = "accent"
                raw = raw[4:]
            elif raw.startswith("```"):
                style = "muted"
            lines.append((style, raw))
        return lines

    def help_lines(self) -> list[str]:
        return [
            "pyPracLab — keys",
            "",
            "Global:  t cycle theme  T shuffle  ? help  q quit",
            "",
            "Main:    arrows move  enter select  1/2/3 Problems/Lessons/Settings",
            "",
            "Lists:   arrows move  enter open  esc/b back",
            "Problems: f favorite  s sort  0/1/2/3 filter all/easy/medium/hard",
            "",
            "Detail:  e edit  r run tests  h hint  y syntax  f favorite",
            "Lessons: e open exercise  arrows scroll",
        ]

    def clamp_index(self, rows: list[ListRow]) -> None:
        if not rows:
            self.index = 0
            return
        self.index = max(0, min(self.index, len(rows) - 1))

    def move_up(self) -> None:
        rows = self.list_rows()
        if not rows:
            return
        self.index = (self.index - 1) % len(rows)

    def move_down(self) -> None:
        rows = self.list_rows()
        if not rows:
            return
        self.index = (self.index + 1) % len(rows)

    def scroll_up(self, amount: int = 1) -> None:
        self.scroll = max(0, self.scroll - amount)

    def scroll_down(self, amount: int, max_scroll: int) -> None:
        self.scroll = min(max_scroll, self.scroll + amount)

    def handle_key(self, key: str | int) -> None:
        if key == -1:
            self.frame += 1
            return

        s = self.screen

        if key == "q" and s.name != "problem_detail":
            if s.name == "help":
                self.pop()
            else:
                self.quit_requested = True
            return
        if key == "?":
            self.push("help")
            return
        if key == "t":
            self.settings.theme = cycle_theme(self.settings.theme)
            self.save_settings()
            return
        if key == "T":
            self.settings.theme = shuffle_theme(self.settings.theme)
            self.save_settings()
            return
        if key in (KEY_ESC, "b"):
            if self._action_back():
                return

        if s.name == "main":
            self._handle_main(key)
        elif s.name == "problems_tracks":
            self._handle_list_nav(key, self._activate_track)
        elif s.name == "problems_list":
            self._handle_problems_list(key)
        elif s.name == "problem_detail":
            self._handle_problem_detail(key)
        elif s.name == "lessons":
            self._handle_lessons(key)
        elif s.name == "lesson_reader":
            self._handle_lesson_reader(key)
        elif s.name == "settings":
            self._handle_settings(key)
        elif s.name == "help":
            if key in (KEY_ESC, "q"):
                self.pop()

    def _handle_main(self, key: str | int) -> None:
        shortcuts = {"1": "problems", "2": "lessons", "3": "settings"}
        if key in shortcuts:
            self._activate_main(shortcuts[key])
            return
        if key in (KEY_UP, KEY_DOWN):
            if key == KEY_UP:
                self.move_up()
            else:
                self.move_down()
            return
        if key == KEY_ENTER:
            rows = self.list_rows()
            self.clamp_index(rows)
            if rows:
                self._activate_main(rows[self.index].key)

    def _activate_main(self, key: str) -> None:
        if key == "problems":
            # land on the first real track by default; Favorites sits above it
            self.push("problems_tracks", default_index=1)
        elif key == "lessons":
            self.lesson_mode = "tracks"
            self.lesson_track = None
            self.push("lessons")
        elif key == "settings":
            self.push("settings")
        elif key == "quit":
            self.quit_requested = True

    def _handle_list_nav(self, key: str | int, activate) -> None:
        if key == KEY_ESC:
            self.pop()
            return
        if key in (KEY_UP, KEY_DOWN):
            if key == KEY_UP:
                self.move_up()
            else:
                self.move_down()
            return
        if key == KEY_ENTER:
            rows = self.list_rows()
            self.clamp_index(rows)
            if rows and rows[self.index].key:
                activate(rows[self.index].key)

    def _activate_track(self, track: str) -> None:
        self.sort = self.settings.default_sort
        self.diff_filter = self.settings.default_difficulty_filter
        self.push("problems_list", track=track)

    def _handle_problems_list(self, key: str | int) -> None:
        if key == KEY_ESC:
            self.pop()
            return
        if key == "f":
            rows = self.list_rows()
            self.clamp_index(rows)
            if rows and rows[self.index].key:
                rel = rows[self.index].key
                if self.toggle_favorite(rel):
                    self.output = "Added to favorites."
                else:
                    self.output = "Removed from favorites."
            return
        if key == "s":
            idx = SORT_MODES.index(self.sort)
            self.sort = SORT_MODES[(idx + 1) % len(SORT_MODES)]
            self.index = 0
            return
        if key == "0":
            self.diff_filter = "all"
            self.index = 0
            return
        if key == "1":
            self.diff_filter = "easy"
            self.index = 0
            return
        if key == "2":
            self.diff_filter = "medium"
            self.index = 0
            return
        if key == "3":
            self.diff_filter = "hard"
            self.index = 0
            return
        if key in (KEY_UP, KEY_DOWN):
            if key == KEY_UP:
                self.move_up()
            else:
                self.move_down()
            return
        if key == KEY_ENTER:
            rows = self.list_rows()
            self.clamp_index(rows)
            if not rows:
                return
            rel = rows[self.index].key
            problems: list[Problem] = self.screen.data.get("problems", [])
            for p in problems:
                if p.rel_path == rel:
                    self.show_hint = self.settings.show_hints_default
                    self.show_syntax = self.settings.show_syntax_hints_default
                    self.push("problem_detail", problem=p)
                    return

    def _handle_problem_detail(self, key: str | int) -> None:
        p: Problem = self.screen.data["problem"]
        if key == KEY_ESC:
            self.pop()
            return
        if key == "h":
            self.show_hint = not self.show_hint
            return
        if key == "y":
            self.show_syntax = not self.show_syntax
            return
        if key == "f":
            if self.toggle_favorite(p.rel_path):
                self.output = "Added to favorites."
            else:
                self.output = "Removed from favorites."
            return
        if key == "e":
            self._open_problem_editor(p)
            return
        if key == "r":
            merge_staged_into_original(p.path)
            self.edit_merge_target = None
            self.output = "Running tests..."
            result = run_problem(p.path)
            if result.ok:
                self.mark_done(p.rel_path)
                msg = "All tests passed."
                if result.output:
                    msg += f"\n{result.output}"
                self.output = msg
            else:
                msg = "Tests failed."
                if result.output:
                    msg += f"\n{result.output}"
                if result.error:
                    msg += f"\n{result.error}"
                self.output = msg
            return

    def _handle_lessons(self, key: str | int) -> None:
        if key == KEY_ESC:
            if self.lesson_mode == "lessons":
                self.lesson_mode = "tracks"
                self.lesson_track = None
                self.index = 0
            else:
                self.pop()
            return
        if key in (KEY_UP, KEY_DOWN):
            if key == KEY_UP:
                self.move_up()
            else:
                self.move_down()
            return
        if key == KEY_ENTER:
            rows = self.list_rows()
            self.clamp_index(rows)
            if not rows:
                return
            name = rows[self.index].key
            if name.startswith("track:"):
                self._remember_index()
                self.lesson_track = name.split(":", 1)[1]
                self.lesson_mode = "lessons"
                self.index = 0
                self._recall_index()
                return
            lessons: list[Lesson] = self.screen.data.get("lessons", [])
            for lesson in lessons:
                if lesson.rel_path == name:
                    self.push("lesson_reader", lesson=lesson)
                    return

    def _handle_lesson_reader(self, key: str | int) -> None:
        if key == KEY_ESC:
            self.pop()
            return
        if key in (KEY_UP, KEY_PAGE_UP):
            self.scroll_up(3 if key == KEY_PAGE_UP else 1)
            return
        if key in (KEY_DOWN, KEY_PAGE_DOWN):
            self.scroll_down(3 if key == KEY_PAGE_DOWN else 1, 99999)
            return
        if key == "e":
            l: Lesson = self.screen.data["lesson"]
            rel = l.exercise_rel_path
            if not rel:
                return
            for p in self.catalog.problems:
                if p.rel_path == rel:
                    self.show_hint = self.settings.show_hints_default
                    self.show_syntax = self.settings.show_syntax_hints_default
                    self.push("problem_detail", problem=p)
                    return

    def _handle_settings(self, key: str | int) -> None:
        if key == KEY_ESC:
            self.pop()
            return
        if key in (KEY_UP, KEY_DOWN):
            if key == KEY_UP:
                self.move_up()
            else:
                self.move_down()
            return
        if key == KEY_ENTER:
            rows = self.list_rows()
            self.clamp_index(rows)
            if rows:
                self._cycle_setting(rows[self.index].key)

    def _cycle_setting(self, attr: str) -> None:
        s = self.settings
        if attr == "editor":
            order = list(EDITOR_CANDIDATES)
            idx = order.index(s.editor) if s.editor in order else 0
            s.editor = order[(idx + 1) % len(order)]
        elif attr == "open_mode":
            idx = OPEN_MODES.index(s.open_mode) if s.open_mode in OPEN_MODES else 0
            s.open_mode = OPEN_MODES[(idx + 1) % len(OPEN_MODES)]
        elif attr == "theme":
            idx = THEME_NAMES.index(s.theme) if s.theme in THEME_NAMES else 0
            s.theme = THEME_NAMES[(idx + 1) % len(THEME_NAMES)]
        elif attr == "default_sort":
            idx = SORT_MODES.index(s.default_sort) if s.default_sort in SORT_MODES else 0
            s.default_sort = SORT_MODES[(idx + 1) % len(SORT_MODES)]
        elif attr == "default_difficulty_filter":
            order = ["all", "easy", "medium", "hard"]
            idx = order.index(s.default_difficulty_filter) if s.default_difficulty_filter in order else 0
            s.default_difficulty_filter = order[(idx + 1) % len(order)]
        elif attr == "terminal":
            order = list(TERMINAL_CANDIDATES)
            idx = order.index(s.terminal) if s.terminal in order else 0
            s.terminal = order[(idx + 1) % len(order)]
        elif attr in ("show_hints_default", "show_syntax_hints_default", "snowfall_enabled"):
            setattr(s, attr, not getattr(s, attr))
        self.save_settings()

    def _open_problem_editor(self, problem: Problem) -> None:
        path, merge_target = prepare_problem_for_edit(
            problem.path,
            show_hint=self.show_hint,
            show_syntax=self.show_syntax,
        )
        self.edit_merge_target = merge_target
        self._open_editor(path)

    def _open_editor(self, path: Path) -> None:
        """Open path in the configured editor without corrupting curses."""
        if self.settings.open_mode == "window" and open_window(self.settings, path):
            self.output = "Opened editor in a new window."
            return
        if self.settings.open_mode == "window":
            term = self.settings.terminal
            self.suspend_message = (
                f"Terminal '{term}' not found — opened here instead."
            )
        else:
            self.suspend_message = "Editor closed."
        self.needs_suspend = path

    def run_suspend(self) -> None:
        """Run editor after curses.endwin(); caller must re-init display."""
        path = self.needs_suspend
        self.needs_suspend = None
        if path is None:
            return
        cmd = _editor_command(self.settings, path)
        subprocess.run(cmd, check=False)
        if self.edit_merge_target is not None:
            merge_staged_into_original(self.edit_merge_target)
            self.edit_merge_target = None
        self.output = self.suspend_message or "Editor closed."

    def animates(self) -> bool:
        return True

    def tick_snow(self, width: int, height: int) -> None:
        """Advance snowfall for the body area."""
        if not self.settings.snowfall_enabled:
            return
        if width < 1 or height < 1:
            return
        size = (width, height)
        if size != self._snow_size:
            self.snow.reset(width, height)
            self._snow_size = size
        self.snow.tick(width, height)
