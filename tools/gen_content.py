"""Turn the specs in tools/specs/ into real problem and lesson files.

This is the main content pipeline: each track has a spec file listing
problems (and optionally lessons) as plain dicts. This script reads all of
them and writes the matching .py/.md files into content/.

Usage:
    python tools/gen_content.py            # write missing files only, skip existing
    python tools/gen_content.py --force    # overwrite every generated file
    python tools/gen_content.py --check    # generate, then verify each problem
                                            # against its reference solution

Problem specs live in PROBLEM_SPECS, lesson specs in LESSON_SPECS — both are
aggregated in tools/specs/__init__.py from the per-track modules.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

PROBLEMS_DIR = ROOT / "content" / "problems"
SOLUTIONS_DIR = ROOT / "content" / "solutions"
LESSONS_DIR = ROOT / "content" / "lessons"


def _indent(text: str, prefix: str = "  ") -> str:
    if not text:
        return ""
    return "\n".join(prefix + line if line else line for line in text.splitlines())


def _comment_block(text: str) -> str:
    """Render a block value as comment lines: '# line' (or '#' for blank lines)."""
    if not text:
        return ""
    out: list[str] = []
    for line in text.splitlines():
        out.append(f"# {line}" if line else "#")
    return "\n".join(out)


def _problem_header(spec: dict) -> str:
    tags = ", ".join(spec.get("tags", []))
    lines = [
        f"# title: {spec['title']}",
        f"# track: {spec['track']}",
        f"# difficulty: {spec['difficulty']}",
    ]
    if tags:
        lines.append(f"# tags: {tags}")
    if spec.get("description"):
        lines.append("# description: |")
        lines.append(_comment_block(spec["description"]))
    if spec.get("examples"):
        lines.append("# examples:")
        lines.append(_comment_block(spec["examples"]))
    if spec.get("hint"):
        lines.append("# hint: |")
        lines.append(_comment_block(spec["hint"]))
    if spec.get("syntax_hint"):
        lines.append("# syntax_hint: |")
        lines.append(_comment_block(spec["syntax_hint"]))
    return "\n".join(lines)


def _problem_body(spec: dict) -> str:
    body = spec["signature"].rstrip() + "\n\n\n"
    body += spec["tests"].rstrip() + "\n\n\n"
    body += 'if __name__ == "__main__":\n    run_tests()\n'
    return body


def write_problem(spec: dict, force: bool) -> Path:
    track = spec["track"]
    diff = spec["difficulty"]
    slug = spec["slug"]
    prob_dir = PROBLEMS_DIR / track / diff
    sol_dir = SOLUTIONS_DIR / track / diff
    prob_dir.mkdir(parents=True, exist_ok=True)
    sol_dir.mkdir(parents=True, exist_ok=True)
    prob_path = prob_dir / f"{slug}.py"
    sol_path = sol_dir / f"{slug}.py"
    content = _problem_header(spec) + "\n\n\n" + _problem_body(spec)
    if force or not prob_path.exists():
        prob_path.write_text(content, encoding="utf-8")
    if force or not sol_path.exists():
        sol_path.write_text(spec["solution"].rstrip() + "\n", encoding="utf-8")
    return prob_path


def write_lesson(spec: dict, force: bool) -> Path:
    track = spec["track"]
    diff = spec["difficulty"]
    slug = spec["slug"]
    lesson_dir = LESSONS_DIR / track / diff
    lesson_dir.mkdir(parents=True, exist_ok=True)
    path = lesson_dir / f"{slug}.md"
    tags = ", ".join(spec.get("tags", []))
    fm = ["---", f"title: {spec['title']}", f"track: {track}", f"difficulty: {diff}"]
    if tags:
        fm.append(f"tags: {tags}")
    if spec.get("exercise"):
        fm.append(f"exercise: {spec['exercise']}")
    fm.append("---")
    content = "\n".join(fm) + "\n\n" + spec["body"].rstrip() + "\n"
    if force or not path.exists():
        path.write_text(content, encoding="utf-8")
    return path


def generate(force: bool) -> None:
    from gen_specs import PROBLEM_SPECS, LESSON_SPECS

    for spec in PROBLEM_SPECS:
        write_problem(spec, force)
    for spec in LESSON_SPECS:
        write_lesson(spec, force)
    print(f"wrote {len(PROBLEM_SPECS)} problems, {len(LESSON_SPECS)} lessons")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    generate(args.force)

    if args.check:
        from pypractlab.runner import verify_problem
        from pypractlab.catalog import load_catalog, lib_available

        cat = load_catalog()
        ok = 0
        fail = 0
        skip = 0
        for p in cat.problems:
            if not lib_available(p.track):
                skip += 1
                continue
            r = verify_problem(p)
            if r.ok:
                ok += 1
            else:
                fail += 1
                print(f"FAIL {p.rel_path}: {r.error or r.output}")
        print(f"ok={ok} fail={fail} skip={skip}")
        raise SystemExit(1 if fail else 0)


if __name__ == "__main__":
    main()
