"""Minimal ASCII rendering for the curses TUI."""

from __future__ import annotations

import curses
import textwrap

from .colors import PAIR_ACCENT, PAIR_ERROR, PAIR_MUTED, PAIR_NORMAL, PAIR_PRIMARY, PAIR_SNOW, PAIR_WARNING
from .controller import AppController, ListRow

STYLE = {
    "normal": PAIR_NORMAL,
    "muted": PAIR_MUTED,
    "primary": PAIR_PRIMARY,
    "title": PAIR_PRIMARY,
    "accent": PAIR_ACCENT,
    "hint": PAIR_WARNING,
    "syntax": PAIR_ACCENT,
    "output": PAIR_ACCENT,
    "error": PAIR_ERROR,
}


def _put(win, y: int, x: int, text: str, attr: int = 0) -> None:
    try:
        h, w = win.getmaxyx()
        if y < 0 or y >= h or x < 0 or x >= w - 1:
            return
        win.addstr(y, x, text[: w - x - 1], attr)
    except curses.error:
        pass


def _list_start(selected: int, count: int, visible: int) -> int:
    """Scroll offset that keeps selection visible without hiding earlier rows unnecessarily."""
    if count <= visible or visible < 1:
        return 0
    start = max(0, min(selected, count - visible))
    return start


def _main_item_heights(rows: list[ListRow]) -> list[int]:
    return [2 if row.detail else 1 for row in rows]


def _main_list_start(selected: int, heights: list[int], visible: int) -> int:
    """Scroll offset for variable-height main menu rows."""
    if not heights or visible < 1:
        return 0
    total = sum(heights)
    if total <= visible:
        return 0
    # Ensure selected row is visible.
    for start in range(len(heights)):
        y = 0
        for i in range(start, len(heights)):
            y += heights[i]
            if i == selected:
                if y <= visible:
                    return start
                break
        if y > visible:
            break
    return max(0, min(selected, len(heights) - 1))


def _preview_attr() -> int:
    attr = curses.color_pair(PAIR_MUTED)
    if curses.has_colors():
        attr |= curses.A_DIM
    return attr


def _menu_label_attr(*, selected: bool, done: bool, favorite: bool = False) -> int:
    if selected:
        return curses.color_pair(PAIR_PRIMARY) | curses.A_BOLD
    if done:
        return curses.color_pair(PAIR_ACCENT)
    if favorite:
        return curses.color_pair(PAIR_WARNING)
    return curses.color_pair(PAIR_NORMAL)


def _menu_detail_attr(*, done: bool, favorite: bool = False) -> int:
    if done:
        return curses.color_pair(PAIR_ACCENT)
    if favorite:
        return curses.color_pair(PAIR_WARNING)
    return curses.color_pair(PAIR_MUTED)


PROBLEM_PREVIEW_MAX_LINES = 4


def _problem_preview_height(list_height: int) -> int:
    """Reserve bottom rows for problem preview (separator + content)."""
    panel = PROBLEM_PREVIEW_MAX_LINES + 1
    if list_height < panel + 3:
        return 0
    return panel


def _draw_problem_preview(
    stdscr,
    lines: list[tuple[str, str]],
    top: int,
    bot: int,
    w: int,
) -> None:
    margin = 4
    width = max(10, w - margin * 2)
    flat: list[tuple[str, str]] = []
    for style, text in lines:
        if not text.strip():
            flat.append((style, ""))
            continue
        for line in textwrap.wrap(text, width=width) or [""]:
            flat.append((style, line))

    _put(stdscr, top, margin, "─" * min(width, w - margin - 1), curses.color_pair(PAIR_MUTED))

    visible = max(0, bot - top - 1)
    for i in range(min(visible, len(flat))):
        style, text = flat[i]
        attr = curses.color_pair(STYLE.get(style, PAIR_NORMAL))
        if style == "title":
            attr |= curses.A_BOLD
        _put(stdscr, top + 1 + i, margin, text, attr)


def draw_frame(stdscr, app: AppController) -> None:
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    if h < 8 or w < 36:
        _put(stdscr, 0, 0, "terminal too small", curses.color_pair(PAIR_ERROR))
        stdscr.refresh()
        return

    _draw_header(stdscr, app, w)
    _draw_footer(stdscr, app, h, w)

    top, bot = 2, h - 2
    if app.settings.snowfall_enabled:
        _draw_snow(stdscr, app, top, bot, w)

    name = app.screen.name

    if name == "main":
        _draw_main(stdscr, app, top, bot, w)
    elif name in ("problems_tracks", "problems_list", "lessons", "settings"):
        _draw_list(stdscr, app, top, bot, w)
    elif name in ("problem_detail", "lesson_reader"):
        lines = app.problem_detail_lines() if name == "problem_detail" else app.lesson_reader_lines()
        _draw_text(stdscr, app, lines, top, bot, w)
    elif name == "help":
        _draw_help(stdscr, top, bot, w)

    stdscr.refresh()


def _draw_header(stdscr, app: AppController, w: int) -> None:
    left = app.header_left()
    right = f"{app.progress_summary()}  {app.settings.theme}"
    _put(stdscr, 0, 2, left, curses.color_pair(PAIR_MUTED))
    _put(stdscr, 0, w - len(right) - 2, right, curses.color_pair(PAIR_MUTED))


def _draw_footer(stdscr, app: AppController, h: int, w: int) -> None:
    parts = [f"{k}:{v}" for k, v in app.footer_hints()]
    line = "  ".join(parts)
    if len(line) > w - 4:
        line = line[: w - 7] + "..."
    _put(stdscr, h - 1, 2, line, curses.color_pair(PAIR_MUTED))


def _draw_snow(stdscr, app: AppController, top: int, bot: int, w: int) -> None:
    """Draw snow in the body area; UI drawn afterward covers flakes under text."""
    snow_attr = curses.color_pair(PAIR_SNOW)
    if curses.has_colors():
        snow_attr |= curses.A_DIM

    for f in app.snow.flakes:
        y = top + int(f.y)
        x = int(f.x)
        if y < top or y >= bot or x < 0 or x >= w - 1:
            continue
        _put(stdscr, y, x, f.char, snow_attr)


def _draw_main(stdscr, app: AppController, top: int, bot: int, w: int) -> None:
    margin = 4
    title_y = top
    menu_top = top + 2

    rows = app.list_rows()
    app.clamp_index(rows)

    _put(stdscr, title_y, margin, "pyPracLab", curses.color_pair(PAIR_PRIMARY) | curses.A_BOLD)
    _draw_main_menu(stdscr, rows, app.index, menu_top, bot, w)


def _draw_main_menu(
    stdscr,
    rows: list[ListRow],
    selected: int,
    top: int,
    bot: int,
    w: int,
) -> None:
    margin = 4
    visible = max(1, bot - top)
    if not rows:
        _put(stdscr, top, margin, "(empty)", curses.color_pair(PAIR_MUTED))
        return

    heights = _main_item_heights(rows)
    start = _main_list_start(selected, heights, visible)
    y = top

    for i in range(start, len(rows)):
        if y >= bot:
            break
        row = rows[i]
        sel = i == selected
        mark = "> " if sel else "  "
        label_attr = (curses.color_pair(PAIR_PRIMARY) | curses.A_BOLD) if sel else curses.color_pair(PAIR_NORMAL)
        _put(stdscr, y, margin, f"{mark}{row.label}", label_attr)
        y += 1
        if row.detail and y < bot:
            preview = row.detail
            max_w = w - margin - 6
            if len(preview) > max_w > 0:
                preview = preview[: max_w - 3] + "..."
            _put(stdscr, y, margin + 4, preview, _preview_attr())
            y += 1

    if sum(heights) > visible:
        if start > 0:
            _put(stdscr, top, w - 6, " more", curses.color_pair(PAIR_MUTED))
        if y >= bot and start + 1 < len(rows):
            _put(stdscr, bot - 1, w - 6, " more", curses.color_pair(PAIR_MUTED))


def _draw_list(stdscr, app: AppController, top: int, bot: int, w: int) -> None:
    margin = 4
    y = top
    crumb = app.breadcrumb()
    if crumb:
        _put(stdscr, y, margin, crumb, curses.color_pair(PAIR_MUTED))
        y += 2

    rows = app.list_rows()
    app.clamp_index(rows)

    list_bot = bot
    preview_lines: list[tuple[str, str]] = []
    if app.screen.name == "problems_list":
        preview_lines = app.problem_list_preview_lines()
        if preview_lines:
            panel_h = _problem_preview_height(bot - y)
            if panel_h:
                list_bot = bot - panel_h

    _draw_menu(stdscr, rows, app.index, y, list_bot, w)

    if preview_lines and list_bot < bot:
        _draw_problem_preview(stdscr, preview_lines, list_bot, bot, w)


def _draw_menu(
    stdscr,
    rows: list[ListRow],
    selected: int,
    top: int,
    bot: int,
    w: int,
) -> None:
    margin = 4
    visible = max(1, bot - top)
    if not rows:
        _put(stdscr, top, margin, "(empty)", curses.color_pair(PAIR_MUTED))
        return

    start = _list_start(selected, len(rows), visible)
    end = min(len(rows), start + visible)

    for i in range(start, end):
        row = rows[i]
        y = top + (i - start)
        if y >= bot:
            break
        sel = i == selected
        mark = "> " if sel else "  "
        label_attr = _menu_label_attr(selected=sel, done=row.done, favorite=row.favorite)
        detail_attr = _menu_detail_attr(done=row.done, favorite=row.favorite)
        line = f"{mark}{row.label}"
        if row.detail and len(line) + len(row.detail) + 3 < w - margin:
            line += f"  {row.detail}"
        _put(stdscr, y, margin, line, label_attr)
        if row.detail and len(f"{mark}{row.label}") + len(row.detail) + 3 >= w - margin:
            _put(stdscr, y, w - len(row.detail) - margin, row.detail, detail_attr)

    if len(rows) > visible:
        if start > 0:
            _put(stdscr, top, w - 6, " more", curses.color_pair(PAIR_MUTED))
        if end < len(rows):
            _put(stdscr, bot - 1, w - 6, " more", curses.color_pair(PAIR_MUTED))


def _draw_text(
    stdscr,
    app: AppController,
    styled: list[tuple[str, str]],
    top: int,
    bot: int,
    w: int,
) -> None:
    margin = 4
    flat: list[tuple[str, str]] = []
    width = max(10, w - margin * 2)
    for style, text in styled:
        if not text.strip():
            flat.append((style, ""))
            continue
        for line in textwrap.wrap(text, width=width) or [""]:
            flat.append((style, line))

    visible = max(1, bot - top)
    max_scroll = max(0, len(flat) - visible)
    app.scroll = min(app.scroll, max_scroll)

    for i in range(visible):
        idx = app.scroll + i
        if idx >= len(flat):
            break
        style, text = flat[idx]
        attr = curses.color_pair(STYLE.get(style, PAIR_NORMAL))
        if style == "title":
            attr |= curses.A_BOLD
        _put(stdscr, top + i, margin, text, attr)

    if max_scroll > 0 and app.scroll > 0:
        _put(stdscr, top, w - 8, f"-{app.scroll}-", curses.color_pair(PAIR_MUTED))


def _draw_help(stdscr, top: int, bot: int, w: int) -> None:
    lines = [
        "keys",
        "",
        "t       cycle color theme",
        "T       shuffle theme",
        "?       help",
        "q       quit",
        "",
        "arrows  move",
        "enter   select",
        "esc     back",
        "",
        "1/2/3   problems / lessons / settings",
        "s       sort problems",
        "0-3     filter difficulty",
        "",
        "e       edit",
        "r       run tests",
        "h       hint",
        "y       syntax hint",
    ]
    for i, line in enumerate(lines):
        y = top + i
        if y >= bot:
            break
        attr = curses.color_pair(PAIR_NORMAL)
        if line == "keys":
            attr = curses.color_pair(PAIR_PRIMARY) | curses.A_BOLD
        _put(stdscr, y, 4, line, attr)
