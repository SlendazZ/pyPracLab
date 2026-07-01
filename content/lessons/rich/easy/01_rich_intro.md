---
title: Rich Terminal Output
track: rich
difficulty: easy
tags: rich, console
exercise: content/problems/rich/easy/01_build_table.py
---

# Rich Terminal Output

## Overview

Rich renders beautiful terminal UI: colors, tables, progress bars, syntax highlighting, markdown, and trees. It detects terminal width and degrades gracefully when color is unavailable.

Plain `print()` dumps raw text. Rich structures output so humans can scan it quickly — especially tables, errors, and nested data.

Real-world uses:

- CLI tools that need readable output for humans (not machines)
- Debug dashboards during long-running data imports
- Pretty-printing nested JSON or config in dev tools
- Status tables in deployment scripts

Install with `pip install rich`. Run `python -m rich` to see a demo of everything Rich can do.

## Console basics

```python
from rich.console import Console

console = Console()
console.print('plain text')
console.print('[bold green]Success[/] operation complete')
console.print({'user': 'Ada', 'score': 98})  # pretty dict
console.print('[red]Error:[/] file not found', style='bold')
```

Markup uses `[style]` tags inspired by BBCode. Close with `[/]` or `[/bold green]`. Common styles: `bold`, `italic`, `dim`, `underline`, and colors like `red`, `cyan`, `bright_white`.

**Worked example:** status messages:

```python
def log_ok(console: Console, msg: str) -> None:
    console.print(f'[green]OK[/] {msg}')

def log_err(console: Console, msg: str) -> None:
    console.print(f'[red]FAIL[/] {msg}')

def log_warn(console: Console, msg: str) -> None:
    console.print(f'[yellow]WARN[/] {msg}')
```

## Tables

Tables are the most common Rich structure in exercises:

```python
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title='Users')
table.add_column('Name', style='cyan')
table.add_column('Score', justify='right', style='magenta')
table.add_row('Ada', '98')
table.add_row('Grace', '95')
console.print(table)
```

Build tables programmatically from data:

```python
users = [('Ada', 98), ('Grace', 95), ('Linus', 88)]
table = Table(title='Leaderboard')
table.add_column('Name')
table.add_column('Score', justify='right')
for name, score in users:
    table.add_row(name, str(score))
assert table.row_count == 3
```

Tables expose `.columns` and `.rows` for testing without rendering ANSI.

**Worked example:** build table from list of dicts:

```python
def build_user_table(records: list[dict]) -> Table:
    table = Table(title='Users')
    table.add_column('ID', justify='right')
    table.add_column('Name')
    table.add_column('Role')
    for r in records:
        table.add_row(str(r['id']), r['name'], r['role'])
    return table

t = build_user_table([{'id': 1, 'name': 'Ada', 'role': 'admin'}])
assert t.row_count == 1
```

## Capturing output in tests

Redirect Console output to a string buffer:

```python
import io
from rich.console import Console

buf = io.StringIO()
console = Console(file=buf, width=80, force_terminal=True)
console.print('[bold]hello[/]')
text = buf.getvalue()
assert 'hello' in text
```

For tables, prefer asserting structure over parsing ANSI escape codes:

```python
assert table.row_count == 2
assert table.columns[0].header == 'Name'
```

## Panels and rules

Group related output visually:

```python
from rich.panel import Panel
from rich.rule import Rule

console.print(Rule('[bold]Results'))
console.print(Panel('Deployment finished successfully.', title='Done', border_style='green'))
console.print(Panel('Connection refused on port 5432.', title='Error', border_style='red'))
```

## Syntax highlighting and JSON

```python
from rich.syntax import Syntax
from rich.json import JSON

code = 'def hello():\n    return 42'
console.print(Syntax(code, 'python', theme='monokai', line_numbers=True))
console.print(JSON('{"active": true, "count": 3}'))
```

Great for CLI tools that display config files or API responses.

## Progress bars (preview)

```python
from rich.progress import track

for item in track(range(100), description='Processing...'):
    ...  # work
```

Rich handles spinner, percentage, and ETA automatically.

## Real-world scenario: deployment summary

```python
from rich.console import Console
from rich.table import Table

def print_deploy_summary(services: list[dict]) -> None:
    console = Console()
    table = Table(title='Deploy Results')
    table.add_column('Service')
    table.add_column('Status', justify='center')
    for svc in services:
        status = '[green]OK[/]' if svc['ok'] else '[red]FAIL[/]'
        table.add_row(svc['name'], status)
    console.print(table)

print_deploy_summary([
    {'name': 'api', 'ok': True},
    {'name': 'worker', 'ok': False},
])
```

## When to use Rich

- CLI tools for humans (not machine-parseable stdout)
- Long scripts where you want visibility without a GUI
- Nested data structures that `print()` makes unreadable

When **not** to use Rich: output piped to another program (`mytool | jq`) — provide a `--plain` flag that prints simple text.

## Common pitfalls

- Parsing ANSI codes in tests — capture via Console or inspect table structure
- Assuming wide terminal — set `width=` in tests for consistent layout
- Rich in CI without `force_terminal=True` when you need styles applied
- Forgetting Rich adds escape codes — `len(output)` != visible character count
- Mixing `print()` and `console.print()` — stick to one Console instance

## Practice

Build a table programmatically and assert row count.

## Summary

Rich = structured terminal rendering. Create `Console`, build data structures (Table, Panel), and let Rich handle layout and color. Test by inspecting table rows/columns or capturing output to a StringIO buffer.
