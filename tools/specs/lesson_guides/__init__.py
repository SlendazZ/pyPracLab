"""Comprehensive lesson guides — documentation-style content for the TUI reader."""

from . import (
    algorithms,
    apis,
    apps,
    automations,
    bs4,
    click,
    fastapi,
    httpx,
    pandas,
    requests,
    rich,
    servers,
    sqlite,
    syntax,
    tkinter,
)

LESSONS: list[dict] = []
for _mod in (
    algorithms,
    syntax,
    automations,
    apis,
    servers,
    apps,
    fastapi,
    requests,
    httpx,
    pandas,
    rich,
    sqlite,
    bs4,
    click,
    tkinter,
):
    LESSONS.extend(_mod.LESSONS)

__all__ = ["LESSONS"]
