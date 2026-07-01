# Map theme tokens to curses color pairs.

from __future__ import annotations

import curses

from ..themes import theme_tokens

PAIR_NORMAL = 1
PAIR_PRIMARY = 2
PAIR_MUTED = 3
PAIR_ACCENT = 4
PAIR_WARNING = 5
PAIR_ERROR = 6
PAIR_SNOW = 7


def _rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return (
        int(h[0:2], 16) * 1000 // 255,
        int(h[2:4], 16) * 1000 // 255,
        int(h[4:6], 16) * 1000 // 255,
    )


def _fg_slot(index: int, hex_color: str) -> int:
    slot = 16 + index
    if curses.can_change_color():
        try:
            curses.init_color(slot, *_rgb(hex_color))
        except curses.error:
            pass
    return slot


def setup_theme(theme_name: str) -> None:
    t = theme_tokens(theme_name)
    curses.start_color()
    try:
        curses.use_default_colors()
    except curses.error:
        pass

    bg = -1

    if curses.can_change_color():
        curses.init_pair(PAIR_NORMAL, _fg_slot(0, t["text"]), bg)
        curses.init_pair(PAIR_PRIMARY, _fg_slot(1, t["primary"]), bg)
        curses.init_pair(PAIR_MUTED, _fg_slot(2, t["muted"]), bg)
        curses.init_pair(PAIR_ACCENT, _fg_slot(3, t["accent"]), bg)
        curses.init_pair(PAIR_WARNING, _fg_slot(4, t["warning"]), bg)
        curses.init_pair(PAIR_ERROR, _fg_slot(5, t["error"]), bg)
        curses.init_pair(PAIR_SNOW, _fg_slot(6, t["muted"]), bg)
    else:
        curses.init_pair(PAIR_NORMAL, curses.COLOR_WHITE, bg)
        curses.init_pair(PAIR_PRIMARY, curses.COLOR_CYAN, bg)
        curses.init_pair(PAIR_MUTED, curses.COLOR_WHITE, bg)
        curses.init_pair(PAIR_ACCENT, curses.COLOR_GREEN, bg)
        curses.init_pair(PAIR_WARNING, curses.COLOR_YELLOW, bg)
        curses.init_pair(PAIR_ERROR, curses.COLOR_RED, bg)
        curses.init_pair(PAIR_SNOW, curses.COLOR_WHITE, bg)
