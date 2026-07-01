# User settings: editor, theme, sort, hint defaults.

from __future__ import annotations

import json
import os
import shlex
import shutil
import sys
import tempfile
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path

from .catalog import ROOT

EDITOR_CANDIDATES_UNIX = ("helix", "micro", "nvim", "vim", "nano", "emacs", "code")
EDITOR_CANDIDATES_WINDOWS = ("code", "notepad", "nvim", "vim", "micro")
EDITOR_CANDIDATES = (
    EDITOR_CANDIDATES_WINDOWS if sys.platform == "win32" else EDITOR_CANDIDATES_UNIX
)

TERMINAL_CANDIDATES_UNIX = (
    "xdg-terminal-exec",
    "foot",
    "kitty",
    "alacritty",
    "ghostty",
    "wezterm",
)
TERMINAL_CANDIDATES_WINDOWS = ("wt", "powershell", "cmd")
TERMINAL_CANDIDATES = (
    TERMINAL_CANDIDATES_WINDOWS if sys.platform == "win32" else TERMINAL_CANDIDATES_UNIX
)


def detect_terminal() -> str:
    env_term = os.environ.get("TERMINAL", "").strip()
    if env_term:
        binary = shlex.split(env_term)[0]
        if shutil.which(binary):
            return binary
    for candidate in TERMINAL_CANDIDATES:
        if shutil.which(candidate):
            return candidate
    return TERMINAL_CANDIDATES[0]


SETTINGS_FILE = ROOT / ".settings.json"

SORT_MODES = ["name", "completion", "difficulty", "number"]
OPEN_MODES = ["inline", "window"]


def _detect_editor() -> str:
    for env_name in ("PRACTICE_EDITOR", "EDITOR"):
        raw = os.environ.get(env_name, "").strip()
        if not raw:
            continue
        binary = shlex.split(raw)[0]
        if binary == "hx":
            return "helix"
        if shutil.which(binary) or binary in EDITOR_CANDIDATES:
            return binary
    for candidate in EDITOR_CANDIDATES:
        if shutil.which(candidate):
            return candidate
    if shutil.which("hx"):
        return "helix"
    return EDITOR_CANDIDATES[0]


def _detect_terminal() -> str:
    return detect_terminal()


@dataclass
class Settings:
    editor: str = field(default_factory=_detect_editor)
    open_mode: str = "window"
    terminal: str = field(default_factory=_detect_terminal)
    theme: str = "yellow"
    default_sort: str = "number"
    default_difficulty_filter: str = "all"
    show_hints_default: bool = False
    show_syntax_hints_default: bool = False
    snowfall_enabled: bool = True

    @classmethod
    def default(cls) -> "Settings":
        return cls()

    @classmethod
    def load(cls) -> "Settings":
        if not SETTINGS_FILE.exists():
            settings = cls.default()
            settings.validate()
            settings.save()
            return settings
        try:
            data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            settings = cls.default()
            settings.validate()
            settings.save()
            return settings
        if not isinstance(data, dict):
            settings = cls.default()
            settings.validate()
            settings.save()
            return settings
        known = {f.name for f in fields(cls)}
        clean = {k: v for k, v in data.items() if k in known}
        settings = cls(**clean)
        before = asdict(settings)
        settings.validate()
        if asdict(settings) != before:
            settings.save()
        return settings

    def save(self) -> None:
        payload = json.dumps(asdict(self), indent=2) + "\n"
        SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(
            dir=SETTINGS_FILE.parent,
            prefix=".settings.",
            suffix=".tmp",
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(payload)
            os.replace(tmp_name, SETTINGS_FILE)
        except OSError:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
            SETTINGS_FILE.write_text(payload, encoding="utf-8")

    def validate(self) -> None:
        from .themes import normalize_theme

        self.theme = normalize_theme(self.theme)
        if self.open_mode not in OPEN_MODES:
            self.open_mode = "inline"
        if self.default_sort not in SORT_MODES:
            self.default_sort = "number"
        if self.default_difficulty_filter not in {"all", "easy", "medium", "hard"}:
            self.default_difficulty_filter = "all"
        if not shutil.which(self.terminal):
            self.terminal = detect_terminal()


PROGRESS_FILE = ROOT / ".progress.json"
FAVORITES_FILE = ROOT / ".favorites.json"


def load_progress() -> dict[str, str]:
    if not PROGRESS_FILE.exists():
        return {}
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    completed = data.get("completed", {})
    if not isinstance(completed, dict):
        return {}
    return {str(k): str(v) for k, v in completed.items()}


def save_progress(completed: dict[str, str]) -> None:
    PROGRESS_FILE.write_text(
        json.dumps({"completed": completed}, indent=2) + "\n", encoding="utf-8"
    )


def load_favorites() -> dict[str, str]:
    if not FAVORITES_FILE.exists():
        return {}
    try:
        data = json.loads(FAVORITES_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    favorites = data.get("favorites", {})
    if not isinstance(favorites, dict):
        return {}
    return {str(k): str(v) for k, v in favorites.items()}


def save_favorites(favorites: dict[str, str]) -> None:
    FAVORITES_FILE.write_text(
        json.dumps({"favorites": favorites}, indent=2) + "\n", encoding="utf-8"
    )
