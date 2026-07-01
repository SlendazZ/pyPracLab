"""Key constants for the ASCII TUI."""

from __future__ import annotations

import curses

KEY_UP = "UP"
KEY_DOWN = "DOWN"
KEY_LEFT = "LEFT"
KEY_RIGHT = "RIGHT"
KEY_ENTER = "ENTER"
KEY_ESC = "ESC"
KEY_BACKSPACE = "BACKSPACE"
KEY_PAGE_UP = "PAGE_UP"
KEY_PAGE_DOWN = "PAGE_DOWN"
KEY_HOME = "HOME"
KEY_END = "END"

_KEY_MAP = {
    curses.KEY_UP: KEY_UP,
    curses.KEY_DOWN: KEY_DOWN,
    curses.KEY_LEFT: KEY_LEFT,
    curses.KEY_RIGHT: KEY_RIGHT,
    curses.KEY_ENTER: KEY_ENTER,
    10: KEY_ENTER,
    13: KEY_ENTER,
    27: KEY_ESC,
    curses.KEY_BACKSPACE: KEY_BACKSPACE,
    127: KEY_BACKSPACE,
    curses.KEY_PPAGE: KEY_PAGE_UP,
    curses.KEY_NPAGE: KEY_PAGE_DOWN,
    curses.KEY_HOME: KEY_HOME,
    curses.KEY_END: KEY_END,
}


def normalize_key(ch: int) -> str | int:
    """Normalize a curses getch result to a string key name or single char."""
    if ch == -1:
        return -1
    if ch in _KEY_MAP:
        return _KEY_MAP[ch]
    if 0 <= ch <= 255:
        try:
            return chr(ch)
        except ValueError:
            return ch
    return ch
