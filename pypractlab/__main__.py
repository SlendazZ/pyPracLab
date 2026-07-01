"""CLI entry point for pyPracLab."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .catalog import ROOT, lib_available, load_catalog
from .models import TRACK_LABELS
from .runner import RunResult, compile_check, run_problem, verify_problem


def _print_result(label: str, result: RunResult) -> bool:
    if result.ok:
        print(f"  ok   {label}")
        return True
    detail = result.error or result.output or "failed"
    print(f"  FAIL {label}: {detail}")
    return False


def cmd_check() -> int:
    cat = load_catalog()
    if not cat.problems:
        print("No problems discovered.")
        return 1

    failed, total, msg = compile_check()
    if failed:
        print(f"Compile-check: {failed}/{total} files failed.")
        print(msg)
        return 1
    print(f"Compile-check: {total} files clean.")

    passed = 0
    skipped = 0
    failed_list: list[str] = []
    for p in cat.problems:
        track = p.track
        if track in TRACK_LABELS and not lib_available(track):
            skipped += 1
            continue
        result = verify_problem(p)
        if _print_result(p.rel_path, result):
            passed += 1
        else:
            failed_list.append(p.rel_path)

    print()
    print(f"verified: {passed}/{len(cat.problems)}  skipped(missing lib): {skipped}")
    if failed_list:
        print(f"failed: {len(failed_list)}")
        for f in failed_list:
            print(f"  - {f}")
        return 1
    return 0


def cmd_self_test() -> int:
    cat = load_catalog()
    failed, total, msg = compile_check()
    if failed:
        print(msg)
        return 1
    print(f"Discovered {len(cat.problems)} problems, {len(cat.lessons)} lessons. "
          f"Compile-check clean ({total} files).")
    for track in cat.tracks_with_problems:
        n = sum(1 for p in cat.problems if p.track == track)
        print(f"  {TRACK_LABELS.get(track, track)}: {n} problems")
    return 0


def cmd_run(path: str) -> int:
    target = Path(path)
    if not target.is_absolute():
        target = (Path.cwd() / path).resolve()
    if not target.exists():
        print(f"not found: {target}")
        return 1
    result = run_problem(target)
    if result.output:
        print(result.output)
    if result.error:
        print(result.error, file=sys.stderr)
    return 0 if result.ok else 1


def main() -> None:
    parser = argparse.ArgumentParser(prog="pypractlab", description="Python practice lab")
    parser.add_argument("--check", action="store_true", help="verify all problems against reference solutions")
    parser.add_argument("--self-test", action="store_true", help="discovery + compile check")
    parser.add_argument("--run", metavar="PATH", help="run a single problem's tests")
    args = parser.parse_args()

    if args.check:
        raise SystemExit(cmd_check())
    if args.self_test:
        raise SystemExit(cmd_self_test())
    if args.run:
        raise SystemExit(cmd_run(args.run))

    from .app import PyPracLabApp
    PyPracLabApp().run()


if __name__ == "__main__":
    main()
