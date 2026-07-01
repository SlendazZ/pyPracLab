---
title: Tables, Panels, and Layout
track: rich
difficulty: medium
tags: rich, layout
exercise: content/problems/rich/easy/04_panel_wrap.py
---

# Tables, Panels, and Layout

## Overview

Beyond single tables, Rich composes layouts: styled columns, stacked panels, and live-updating displays. This lesson covers structuring CLI dashboards that stay readable in narrow terminals.

Real-world uses:

- Deployment dashboards (service status side by side)
- Test runners showing pass/fail panels per suite
- Download managers with live progress tables
- Log tailers with highlighted error panels

## Table styling in depth

```python
from rich.table import Table

table = Table(
    title='Service Health',
    show_header=True,
    header_style='bold magenta',
    border_style='blue',
    show_lines=True,
)
table.add_column('ID', style='dim', width=6)
table.add_column('Service', min_width=12)
table.add_column('Status', justify='center')
table.add_column('Latency', justify='right')
table.add_row('1', 'api-gateway', '[green]OK[/]', '42ms')
table.add_row('2', 'worker', '[red]DOWN[/]', '-')
```

Column `width` fixes size; `min_width`/`max_width` constrain flexible columns. `justify` controls alignment: `left`, `center`, `right`.

**Worked example:** build status table from dicts:

```python
services = [
    {'id': 1, 'name': 'api', 'ok': True, 'ms': 42},
    {'id': 2, 'name': 'db', 'ok': False, 'ms': None},
]
table = Table(title='Health')
table.add_column('ID', justify='right')
table.add_column('Name')
table.add_column('Status', justify='center')
table.add_column('Latency', justify='right')
for s in services:
    status = '[green]OK[/]' if s['ok'] else '[red]FAIL[/]'
    latency = f"{s['ms']}ms" if s['ms'] is not None else '-'
    table.add_row(str(s['id']), s['name'], status, latency)
```

## Panel variants

Panels wrap content with a border and optional title:

```python
from rich.panel import Panel
from rich.text import Text

error = Text.from_markup('[red]Error[/]: connection timeout after 30s')
panel = Panel(error, title='API', border_style='red', expand=False)
console.print(panel)
```

Wrap long text with explicit width:

```python
Panel('Short status message.', title='Build #42', border_style='green')
Panel(long_log_text, title='stderr', width=80)
```

**Worked example:** wrap status in a panel (exercise pattern):

```python
def make_status_panel(message: str, title: str = 'Status') -> Panel:
    return Panel(message, title=title, border_style='blue', expand=False)

p = make_status_panel('All systems operational')
assert p.title == 'Status'
assert p.renderable == 'All systems operational'
```

## Columns layout

Display panels side by side:

```python
from rich.columns import Columns

ok_panel = Panel('All tests passed', title='Unit', border_style='green')
warn_panel = Panel('2 warnings', title='Lint', border_style='yellow')
console.print(Columns([ok_panel, warn_panel], equal=True, expand=True))
```

Rich reflows columns when the terminal is too narrow.

## Live display

Update a table in place without flooding scrollback:

```python
import time
from rich.live import Live
from rich.table import Table

table = Table()
table.add_column('Step')
table.add_column('Status')

with Live(table, refresh_per_second=4):
    for step in ['fetch', 'validate', 'upload', 'done']:
        table.add_row(step, 'running...')
        time.sleep(0.5)
        table.rows[-1] = (step, '[green]done[/]')
```

Use `Live` for progress dashboards; use `track` for simple loops.

## Tree and Markdown

```python
from rich.tree import Tree
from rich.markdown import Markdown

tree = Tree('[bold]Project[/]')
src = tree.add('[cyan]src[/]')
src.add('main.py')
src.add('utils.py')
console.print(tree)

console.print(Markdown('# Release Notes\n\n- Fixed login bug\n- Updated deps'))
```

## Group and Align

```python
from rich.align import Align
from rich.console import Group

console.print(Align.center('[bold]Deploy Summary[/]'))
console.print(Group(panel_a, panel_b, table))
```

## Real-world scenario: test runner dashboard

```python
def print_test_results(results: list[dict]) -> None:
    passed = sum(1 for r in results if r['passed'])
    failed = len(results) - passed
    summary = Panel(
        f'[green]{passed} passed[/]  [red]{failed} failed[/]',
        title='Summary',
        border_style='cyan',
    )
    table = Table(title='Failures')
    table.add_column('Test')
    table.add_column('Error')
    for r in results:
        if not r['passed']:
            table.add_row(r['name'], r['error'])
    console.print(Group(summary, table))
```

## Testing structured output

Assert on data, not rendered strings:

```python
def make_panel(message: str, title: str) -> Panel:
    return Panel(message, title=title, border_style='blue')

p = make_panel('ready', 'Status')
assert p.title == 'Status'
assert p.renderable == 'ready'
```

For tables: check `table.row_count`, column headers, and cell values before calling `console.print()`.

## Common pitfalls

- Live display without bounding rows — table grows forever; replace rows or clear periodically
- Nested panels exceeding terminal height — use `height=` or scroll in an external pager
- Hard-coding Unicode box chars — use Rich primitives so width math works
- Mixing `print()` and `console.print()` — stick to one Console instance
- Forgetting `expand=False` on panels in narrow layouts

## Practice

Wrap status text in a styled panel with a title.

## Summary

Compose small Rich objects into layouts. Style tables with column width and justify; wrap messages in Panels; place panels side by side with Columns; use Live for in-place updates. Test the objects you build, not the ANSI output.
