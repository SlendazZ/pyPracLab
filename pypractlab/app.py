# Application entry.

from __future__ import annotations

from .tui.loop import run_tui


class PyPracLabApp:
    def run(self) -> None:
        run_tui()
