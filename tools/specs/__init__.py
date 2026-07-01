"""Aggregate all per-track spec modules."""

from . import (
    algorithms,
    apis,
    apps,
    automations,
    bulk_additions,
    bs4,
    click,
    extras,
    fastapi,
    httpx,
    lesson_guides,
    pandas,
    requests,
    rich,
    servers,
    sqlite,
    syntax,
    tkinter,
)

PROBLEM_SPECS: list[dict] = []
LESSON_SPECS: list[dict] = list(lesson_guides.LESSONS)

for _mod in (
    algorithms,
    syntax,
    automations,
    apis,
    servers,
    apps,
    fastapi,
    tkinter,
    requests,
    httpx,
    pandas,
    rich,
    sqlite,
    bs4,
    click,
    extras,
    bulk_additions,
):
    PROBLEM_SPECS.extend(getattr(_mod, "PROBLEMS", []))

__all__ = ["PROBLEM_SPECS", "LESSON_SPECS"]
