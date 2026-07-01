# Curses main loop.

from __future__ import annotations

import curses
import sys

from .colors import setup_theme
from .controller import AppController
from .keys import normalize_key
from .render import draw_frame


def _run_loop(stdscr) -> None:
    curses.curs_set(0)
    stdscr.keypad(True)
    # keep Esc responsive for arrow-key sequences
    if hasattr(curses, "set_escdelay"):
        curses.set_escdelay(25)

    app = AppController()
    applied_theme: str | None = None

    while not app.quit_requested:
        if app.settings.theme != applied_theme:
            setup_theme(app.settings.theme)
            applied_theme = app.settings.theme

        h, w = stdscr.getmaxyx()
        stdscr.timeout(150)
        app.tick_snow(w, max(8, h - 4))

        draw_frame(stdscr, app)

        if app.needs_suspend is not None:
            curses.endwin()
            app.run_suspend()
            # reset terminal after editors that use the alt screen
            sys.stdout.write("\033[?1049l\033[?25h\033[0m\033[2J\033[H")
            sys.stdout.flush()
            stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            stdscr.keypad(True)
            curses.curs_set(0)
            if hasattr(curses, "set_escdelay"):
                curses.set_escdelay(25)
            curses.flushinp()
            stdscr.clear()
            stdscr.refresh()
            applied_theme = None
            continue

        ch = stdscr.getch()
        key = normalize_key(ch)
        app.handle_key(key)


def run_tui() -> None:
    curses.wrapper(_run_loop)
