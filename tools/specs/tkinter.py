"""tkinter problem specs.

These problems import tkinter (so they require `python-tk` to run), but every
run_tests() exercises pure helper logic without opening a Tk window. This keeps
them testable headlessly while still teaching Tkinter patterns.
"""

PROBLEMS = [
    {
        "slug": "01_label_specs",
        "track": "tkinter", "difficulty": "easy",
        "title": "Tkinter Label Specs",
        "tags": ["tkinter", "dict"],
        "description": "Given a list of (key, text) pairs, return label specs: dicts like {\"key\": key, \"text\": text, \"anchor\": \"w\"}.",
        "examples": 'label_specs([("name", "Name:")]) -> [{"key":"name","text":"Name:","anchor":"w"}]',
        "hint": "A list comprehension building dicts is all you need here.",
        "syntax_hint": '[{"key": k, "text": t, "anchor": "w"} for k, t in pairs]',
        "signature": "def label_specs(pairs: list[tuple[str, str]]) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert label_specs([("name", "Name:")]) == [{"key": "name", "text": "Name:", "anchor": "w"}]\n'
            "    assert label_specs([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401  (exercises the import; no window opened)\n\n"
            "def label_specs(pairs: list[tuple[str, str]]) -> list[dict]:\n"
            "    return [{\"key\": k, \"text\": t, \"anchor\": \"w\"} for k, t in pairs]\n"
        ),
    },
    {
        "slug": "02_grid_layout",
        "track": "tkinter", "difficulty": "easy",
        "title": "Grid Layout Planner",
        "tags": ["tkinter", "grid"],
        "description": "Given a list of (widget_name, row, col), return a list of dicts {\"widget\", \"row\", \"col\", \"sticky\": \"ew\"} ready for grid().",
        "examples": 'plan([("a", 0, 0)]) -> [{"widget":"a","row":0,"col":0,"sticky":"ew"}]',
        "hint": "Build dicts with the sticky default added.",
        "syntax_hint": '[{"widget": n, "row": r, "col": c, "sticky": "ew"} for n, r, c in specs]',
        "signature": "def plan(specs: list[tuple[str, int, int]]) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert plan([("a", 0, 0), ("b", 0, 1)]) == [\n'
            '        {"widget": "a", "row": 0, "col": 0, "sticky": "ew"},\n'
            '        {"widget": "b", "row": 0, "col": 1, "sticky": "ew"},\n'
            "    ]\n"
            "    assert plan([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def plan(specs: list[tuple[str, int, int]]) -> list[dict]:\n"
            "    return [{\"widget\": n, \"row\": r, \"col\": c, \"sticky\": \"ew\"} for n, r, c in specs]\n"
        ),
    },
    {
        "slug": "03_validate_numeric_entry",
        "track": "tkinter", "difficulty": "easy",
        "title": "Validate Numeric Entry",
        "tags": ["tkinter", "validation"],
        "description": "Return True if the entry text is a non-negative integer (the kind of check a Tk validation command would use).",
        "examples": 'is_nonneg("123") -> True\nis_nonneg("-1") -> False\nis_nonneg("") -> True',
        "hint": "str.isdigit() is True for non-negative integers and for the empty string is False—handle empty as valid.",
        "syntax_hint": "return s == '' or s.isdigit()",
        "signature": "def is_nonneg(s: str) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert is_nonneg("123") is True\n'
            '    assert is_nonneg("-1") is False\n'
            '    assert is_nonneg("") is True\n'
            '    assert is_nonneg("12a") is False\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def is_nonneg(s: str) -> bool:\n"
            "    return s == '' or s.isdigit()\n"
        ),
    },
    {
        "slug": "04_menu_tree",
        "track": "tkinter", "difficulty": "medium",
        "title": "Menu Tree Builder",
        "tags": ["tkinter", "menu"],
        "description": "Given a nested spec like {'File': {'Open': None, 'Quit': None}, 'Help': {}}, return a flat list of (label_path) strings like 'File > Open', 'File > Quit'. Items with a non-empty dict recurse; None means a leaf.",
        "examples": "paths({'File': {'Open': None}}) -> ['File > Open']",
        "hint": "Recurse, joining the current label with ' > '.",
        "syntax_hint": "if value is None: append(path) else: recurse(value, path)",
        "signature": "def paths(spec: dict) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    spec = {'File': {'Open': None, 'Quit': None}, 'Help': {'About': None}}\n"
            "    assert sorted(paths(spec)) == ['File > Open', 'File > Quit', 'Help > About']\n"
            "    assert paths({}) == []\n"
            "    assert paths({'X': None}) == ['X']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def paths(spec: dict) -> list[str]:\n"
            "    result: list[str] = []\n"
            "    def walk(node, prefix):\n"
            "        for label, value in node.items():\n"
            "            path = f'{prefix} > {label}' if prefix else label\n"
            "            if value is None:\n"
            "                result.append(path)\n"
            "            else:\n"
            "                walk(value, path)\n"
            "    walk(spec, '')\n"
            "    return result\n"
        ),
    },
    {
        "slug": "05_pack_specs",
        "track": "tkinter", "difficulty": "easy",
        "title": "Pack Side Specs",
        "tags": ["tkinter", "pack"],
        "description": "Given a list of (widget, side) where side is 'top' or 'bottom', return pack specs: {'widget', 'side', 'fill': 'x'}.",
        "examples": "pack_specs([('a','top')]) -> [{'widget':'a','side':'top','fill':'x'}]",
        "hint": "A comprehension builds the spec dicts.",
        "syntax_hint": "[{'widget': w, 'side': s, 'fill': 'x'} for w, s in items]",
        "signature": "def pack_specs(items: list[tuple[str, str]]) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert pack_specs([('a', 'top'), ('b', 'bottom')]) == [\n"
            "        {'widget': 'a', 'side': 'top', 'fill': 'x'},\n"
            "        {'widget': 'b', 'side': 'bottom', 'fill': 'x'},\n"
            "    ]\n"
            "    assert pack_specs([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def pack_specs(items: list[tuple[str, str]]) -> list[dict]:\n"
            "    return [{'widget': w, 'side': s, 'fill': 'x'} for w, s in items]\n"
        ),
    },
    {
        "slug": "06_color_specs",
        "track": "tkinter", "difficulty": "easy",
        "title": "Color Specs",
        "tags": ["tkinter", "color"],
        "description": "Given a list of (label, hex_color), validate and return specs whose 'bg' is the hex color only if it matches #RRGGBB, else 'white'.",
        "examples": 'color_specs([("a","#ff0000"),("b","nope")]) -> [{"label":"a","bg":"#ff0000"},{"label":"b","bg":"white"}]',
        "hint": "re.fullmatch(r'#[0-9a-fA-F]{6}', color).",
        "syntax_hint": "re.fullmatch(r'#[0-9a-fA-F]{6}', color) is not None",
        "signature": "def color_specs(items: list[tuple[str, str]]) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert color_specs([('a', '#ff0000'), ('b', 'nope')]) == [\n"
            "        {'label': 'a', 'bg': '#ff0000'},\n"
            "        {'label': 'b', 'bg': 'white'},\n"
            "    ]\n"
            "    assert color_specs([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import re\nimport tkinter  # noqa: F401\n\n"
            "def color_specs(items: list[tuple[str, str]]) -> list[dict]:\n"
            "    out = []\n"
            "    for label, color in items:\n"
            "        bg = color if re.fullmatch(r'#[0-9a-fA-F]{6}', color) else 'white'\n"
            "        out.append({'label': label, 'bg': bg})\n"
            "    return out\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_tkinter_intro",
        "track": "tkinter", "difficulty": "easy",
        "title": "Tkinter Without a Window",
        "tags": ["tkinter"],
        "exercise": "content/problems/tkinter/easy/02_grid_layout.py",
        "body": (
            "# Tkinter\n\n"
            "`tkinter` is Python's standard GUI toolkit. On most Linux installs you need "
            "`pacman -S python-tk` before you can `import tkinter`.\n\n"
            "A typical widget needs layout data (grid position, side, sticky) and "
            "validation logic. Both can be built and tested as **plain data** before any "
            "window is created — that's what these exercises do, so they run headlessly.\n\n"
            "When you do open a window:\n\n"
            "```python\nimport tkinter as tk\nroot = tk.Tk()\nroot.mainloop()\n```"
        ),
    },
]
