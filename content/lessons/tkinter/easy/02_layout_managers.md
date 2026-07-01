---
title: Grid and Pack Layout
track: tkinter
difficulty: easy
tags: tkinter, layout
exercise: content/problems/tkinter/easy/05_pack_specs.py
---

# Grid and Pack Layout

## Overview

Layout managers position widgets inside their parent. **grid** suits forms and calculators; **pack** suits toolbars and simple vertical stacks. Most real apps combine both by nesting `Frame` widgets.

Real-world uses:

- Email client: pack toolbar top, pack status bar bottom, grid message list
- Calculator: grid for the button pad, pack for the display
- IDE-style app: pack sidebar + main area, grid tabs inside main area

## grid in detail

Each widget gets a `(row, column)` address. Rows and columns start at 0.

```python
label.grid(row=0, column=0, sticky='e', padx=5, pady=2)
entry.grid(row=0, column=1, sticky='we', padx=5)
button.grid(row=1, column=0, columnspan=2, pady=8)
```

Key options:

| Option       | Meaning                                      |
|--------------|----------------------------------------------|
| `row`, `column` | Cell address (0-based)                    |
| `sticky`     | Anchor within cell: `n`, `s`, `e`, `w` or combos |
| `padx`, `pady` | External padding (pixels)                |
| `columnspan` | Widget spans multiple columns                |
| `rowspan`    | Widget spans multiple rows                   |

**sticky cheat sheet:**

```
  n
w + e   (ew = stretch horizontally)
  s
nsew    (fill entire cell)
```

**Worked example:** calculator button pad:

```python
BUTTONS = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2),
]

def button_grid_specs() -> list[dict]:
    return [
        {'widget': label, 'row': r, 'col': c, 'sticky': 'nsew'}
        for label, r, c in BUTTONS
    ]
```

Make every column and row equal width with weights:

```python
for col in range(3):
    parent.columnconfigure(col, weight=1, uniform='btn')
for row in range(4):
    parent.rowconfigure(row, weight=1, uniform='btn')
```

## Configuring stretch

Without `weight`, extra window space stays empty:

```python
parent.columnconfigure(1, weight=1)  # column 1 expands horizontally
parent.rowconfigure(0, weight=1)   # row 0 expands vertically
entry.grid(row=0, column=1, sticky='nsew')  # entry fills growing cell
```

Use `uniform='group'` when multiple columns should share space equally (calculator buttons, equal-width form columns).

## pack in detail

Pack stacks widgets along one side of the parent. **Order matters** — the first widget packed gets priority along that side.

```python
toolbar.pack(side='top', fill='x')       # full-width bar at top
content.pack(expand=True, fill='both')   # middle grows
status.pack(side='bottom', fill='x')     # full-width bar at bottom
```

| Option    | Meaning                                           |
|-----------|---------------------------------------------------|
| `side`    | `top`, `bottom`, `left`, `right`                  |
| `fill`    | `x`, `y`, or `both` — stretch to fill parent axis |
| `expand`  | Widget gets extra space when window grows         |
| `padx/pady` | External padding                              |

**Worked example:** pack specs as data (matches the exercise pattern):

```python
def pack_specs(items: list[tuple[str, str]]) -> list[dict]:
    """Convert (widget_name, side) to pack() keyword dicts."""
    return [
        {'widget': widget, 'side': side, 'fill': 'x'}
        for widget, side in items
    ]

specs = pack_specs([('toolbar', 'top'), ('status', 'bottom')])
# [{'widget': 'toolbar', 'side': 'top', 'fill': 'x'},
#  {'widget': 'status', 'side': 'bottom', 'fill': 'x'}]
```

Apply specs to real widgets:

```python
widgets = {'toolbar': toolbar_frame, 'status': status_label}
for spec in pack_specs([('toolbar', 'top'), ('status', 'bottom')]):
    widgets[spec['widget']].pack(side=spec['side'], fill=spec['fill'])
```

## Pack order and priority

Packing `top` then `bottom` reserves space from both edges inward:

```
┌─────────────────────┐
│ toolbar  (top)      │
├─────────────────────┤
│                     │
│ content (expand)    │
│                     │
├─────────────────────┤
│ status   (bottom)   │
└─────────────────────┘
```

If you pack `bottom` first, then `top`, the visual result is the same — but packing `content` last with `expand=True` ensures it fills the middle.

```python
def pack_order(specs: list[dict]) -> list[str]:
    """Return widget names in recommended pack sequence."""
    priority = {'top': 0, 'bottom': 1, 'left': 2, 'right': 3}
    return [s['widget'] for s in sorted(specs, key=lambda s: priority[s['side']])]
```

## Nesting frames: the professional pattern

Combine pack regions with grid forms inside each region:

```python
root = tk.Tk()

toolbar = tk.Frame(root)
toolbar.pack(side='top', fill='x')
tk.Button(toolbar, text='Open').pack(side='left', padx=4)
tk.Button(toolbar, text='Save').pack(side='left', padx=4)

form = tk.Frame(root)
form.pack(expand=True, fill='both', padx=10, pady=10)
tk.Label(form, text='Name:').grid(row=0, column=0, sticky='e')
tk.Entry(form).grid(row=0, column=1, sticky='ew')
form.columnconfigure(1, weight=1)

status = tk.Label(root, text='Ready', anchor='w')
status.pack(side='bottom', fill='x')
root.mainloop()
```

Each frame is its own layout island — pack inside the root, grid inside the form frame.

## Choosing grid vs pack

| Scenario                    | Manager | Why                          |
|-----------------------------|---------|------------------------------|
| Labeled input form          | grid    | aligned columns and rows     |
| Toolbar with buttons        | pack    | horizontal strip             |
| Log output below controls   | pack    | top controls, bottom log     |
| Keyboard / calculator pad   | grid    | uniform button grid          |
| Sidebar + main content      | pack    | left sidebar, right body     |

## Validation without GUI

Exercises test pure functions on layout specs:

```python
def validate_grid(specs: list[dict]) -> bool:
    cells = [(s['row'], s['col']) for s in specs]
    return len(cells) == len(set(cells))  # no duplicate cells

def validate_pack_sides(specs: list[dict]) -> bool:
    allowed = {'top', 'bottom', 'left', 'right'}
    return all(s['side'] in allowed for s in specs)
```

Detect grid collisions (two widgets same row/column), verify pack sides are valid, and confirm sticky values use only `n`, `s`, `e`, `w`.

## Real-world scenario: three-pane editor

```python
def editor_layout() -> dict:
    return {
        'pack': [
            {'widget': 'menu_bar', 'side': 'top', 'fill': 'x'},
            {'widget': 'main_pane', 'side': 'top', 'fill': 'both', 'expand': True},
            {'widget': 'status_bar', 'side': 'bottom', 'fill': 'x'},
        ],
        'grid_inside_main': [
            {'widget': 'file_tree', 'row': 0, 'col': 0, 'sticky': 'ns'},
            {'widget': 'editor', 'row': 0, 'col': 1, 'sticky': 'nsew'},
        ],
    }
```

Pack the outer shell; grid the inner split. Column 1 gets `weight=1` so the editor expands.

## Common pitfalls

- Forgetting `sticky='we'` on `Entry` — field stays tiny when window grows
- `grid` without `columnconfigure` — labels clip on resize
- Duplicate `(row, column)` assignments — second widget hides the first
- Packing `content` before `toolbar` without `expand` — middle does not fill
- Using `place` for entire layouts — hard to maintain; prefer grid/pack

## Practice

Determine correct pack order for top/content/bottom regions.

## Summary

grid = 2D coordinates + sticky + weight. pack = side + fill + expand. Nest frames to combine both in complex UIs. Express layouts as testable spec dicts, then apply them when building real widgets.
