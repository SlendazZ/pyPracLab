# Color themes for the TUI.

from __future__ import annotations

import random

THEMES: dict[str, dict[str, str]] = {
    "blue": {
        "background": "#0d1117",
        "text": "#c9d1d9",
        "muted": "#484f58",
        "primary": "#58a6ff",
        "accent": "#3fb950",
        "warning": "#d29922",
        "error": "#f85149",
    },
    "green": {
        "background": "#0d1a0d",
        "text": "#d4e8d4",
        "muted": "#4a5a4a",
        "primary": "#56d364",
        "accent": "#7ee787",
        "warning": "#e3b341",
        "error": "#ff7b72",
    },
    "cyan": {
        "background": "#0a1628",
        "text": "#cdd9e5",
        "muted": "#445566",
        "primary": "#39c5cf",
        "accent": "#56d4dd",
        "warning": "#e3b341",
        "error": "#ff7b72",
    },
    "yellow": {
        "background": "#1a1608",
        "text": "#e6e0c8",
        "muted": "#5a5540",
        "primary": "#e3b341",
        "accent": "#f0c040",
        "warning": "#d29922",
        "error": "#ff7b72",
    },
    "magenta": {
        "background": "#1a0d1a",
        "text": "#e8d4e8",
        "muted": "#5a4a5a",
        "primary": "#d2a8ff",
        "accent": "#bc8cff",
        "warning": "#e3b341",
        "error": "#ff7b72",
    },
}

THEME_NAMES = ["yellow", "blue", "green", "cyan", "magenta"]

LEGACY_THEMES: dict[str, str] = {
    "midnight": "blue",
    "nord": "cyan",
    "ocean": "cyan",
    "forest": "green",
    "solar": "yellow",
    "rose": "magenta",
}


def normalize_theme(name: str) -> str:
    name = LEGACY_THEMES.get(name, name)
    return name if name in THEMES else THEME_NAMES[0]


def theme_tokens(name: str) -> dict[str, str]:
    return THEMES[normalize_theme(name)]


def cycle_theme(name: str) -> str:
    name = normalize_theme(name)
    idx = THEME_NAMES.index(name)
    return THEME_NAMES[(idx + 1) % len(THEME_NAMES)]


def shuffle_theme(name: str) -> str:
    name = normalize_theme(name)
    candidates = [t for t in THEME_NAMES if t != name]
    return random.choice(candidates) if candidates else name


def theme_obj(name: str) -> dict[str, str]:
    n = normalize_theme(name)
    return {"name": n, **THEMES[n]}
