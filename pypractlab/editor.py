# Open a file in the user's editor, inline or in a new window.

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

from .settings import TERMINAL_CANDIDATES, Settings, detect_terminal

TERMINAL_CANDIDATES = TERMINAL_CANDIDATES


def _editor_command(settings: Settings, target: Path) -> list[str]:
    parts = shlex.split(settings.editor)
    if not parts:
        parts = ["helix"]
    binary = parts[0]
    if not shutil.which(binary):
        if binary == "helix" and shutil.which("hx"):
            parts[0] = "hx"
    return parts + [str(target.resolve())]


def _terminal_command(term: str, editor_cmd: list[str]) -> list[str]:
    if term == "alacritty":
        return ["alacritty", "-e", *editor_cmd]
    if term == "kitty":
        return ["kitty", *editor_cmd]
    if term == "foot":
        return ["foot", *editor_cmd]
    if term == "ghostty":
        return ["ghostty", "-e", *editor_cmd]
    if term == "wezterm":
        return ["wezterm", "start", "--", *editor_cmd]
    if term == "xdg-terminal-exec":
        return ["xdg-terminal-exec", "--", *editor_cmd]
    if term == "wt":
        return ["wt", "-w", "0", *editor_cmd]
    if term == "powershell":
        return [
            "powershell",
            "-NoExit",
            "-Command",
            " ".join(shlex.quote(part) for part in editor_cmd),
        ]
    if term == "cmd":
        return ["cmd", "/c", "start", "", *editor_cmd]
    return [term, "-e", *editor_cmd]


def open_inline(settings: Settings, target: Path) -> None:
    subprocess.run(_editor_command(settings, target), check=False)


def open_window(settings: Settings, target: Path) -> bool:
    term = settings.terminal or detect_terminal()
    if not shutil.which(term):
        return False
    editor_cmd = _editor_command(settings, target)
    cmd = _terminal_command(term, editor_cmd)
    env = dict(os.environ)
    env.setdefault("TERM", "xterm-256color")
    popen_kwargs: dict = {
        "env": env,
        "stdout": subprocess.DEVNULL,
        "stderr": subprocess.DEVNULL,
    }
    if sys.platform != "win32":
        popen_kwargs["start_new_session"] = True
    try:
        subprocess.Popen(cmd, **popen_kwargs)
        return True
    except OSError:
        return False


def open_file(settings: Settings, target: Path) -> str:
    if settings.open_mode == "window":
        if open_window(settings, target):
            return "window"
        return "inline"
    open_inline(settings, target)
    return "inline"
