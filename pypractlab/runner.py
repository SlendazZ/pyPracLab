# Run problem tests, verify solutions, compile-check.

from __future__ import annotations

import importlib.util
import io
import subprocess
import sys
from dataclasses import dataclass
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

from .catalog import ROOT
from .models import Problem


@dataclass
class RunResult:
    ok: bool
    output: str
    error: str = ""


def _load_module(path: Path, name: str | None = None):
    mod_name = name or f"_pypractlab_{abs(hash(str(path)))}"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    old_path = list(sys.path)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path = old_path
    return module


def run_problem(path: Path) -> RunResult:
    out = io.StringIO()
    err = io.StringIO()
    try:
        with redirect_stdout(out), redirect_stderr(err):
            module = _load_module(path)
            run_tests = getattr(module, "run_tests", None)
            if run_tests is None:
                return RunResult(False, "", f"{path.name} has no run_tests() function")
            run_tests()
    except AssertionError as e:
        msg = str(e) or "assertion failed"
        return RunResult(False, out.getvalue().strip(), msg)
    except Exception as e:  # noqa: BLE001
        return RunResult(False, out.getvalue().strip(), f"{type(e).__name__}: {e}")
    return RunResult(True, out.getvalue().strip(), err.getvalue().strip())


def _function_names(problem_module) -> list[str]:
    names = []
    for key, value in vars(problem_module).items():
        if key.startswith("_") or key == "run_tests":
            continue
        if callable(value) and getattr(value, "__module__", "") == problem_module.__name__:
            names.append(key)
    return names


def verify_problem(problem: Problem) -> RunResult:
    if not problem.has_solution:
        return RunResult(False, "", "no reference solution")

    stub_result = run_problem(problem.path)
    if stub_result.ok:
        return RunResult(
            False,
            "",
            "stub unexpectedly passed; test does not exercise the solution",
        )

    out = io.StringIO()
    err = io.StringIO()
    try:
        with redirect_stdout(out), redirect_stderr(err):
            problem_module = _load_module(problem.path, name=f"_stub_{problem.slug}")
            ref_module = _load_module(
                problem.solution_path, name=f"_sol_{problem.slug}"
            )
            for fname in _function_names(problem_module):
                ref_func = getattr(ref_module, fname, None)
                if ref_func is None:
                    continue
                setattr(problem_module, fname, ref_func)
            run_tests = getattr(problem_module, "run_tests", None)
            if run_tests is None:
                return RunResult(False, "", "no run_tests()")
            run_tests()
    except AssertionError as e:
        msg = str(e) or "assertion failed"
        return RunResult(False, out.getvalue().strip(), f"reference failed: {msg}")
    except Exception as e:  # noqa: BLE001
        return RunResult(False, out.getvalue().strip(), f"reference error: {type(e).__name__}: {e}")
    return RunResult(True, out.getvalue().strip(), err.getvalue().strip())


def compile_check(paths: list[Path] | None = None) -> tuple[int, int, str]:
    if paths is None:
        paths = sorted((ROOT / "content").rglob("*.py"))
        paths += sorted((ROOT / "pypractlab").rglob("*.py"))
    failed = 0
    messages: list[str] = []
    for path in paths:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            failed += 1
            messages.append(result.stderr.strip())
    return failed, len(paths), "\n".join(messages)
