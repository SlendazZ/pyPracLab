"""rich problem specs."""

PROBLEMS = [
    {
        "slug": "01_build_table",
        "track": "rich", "difficulty": "easy",
        "title": "Build a Rich Table",
        "tags": ["rich", "table"],
        "description": "Given a list of column headers and a list of row tuples, build and return a rich.table.Table with those columns and rows.",
        "examples": 'build_table(["a","b"], [("1","2")]) -> Table',
        "hint": "from rich.table import Table; add_column / add_row.",
        "syntax_hint": "table = Table(); table.add_column(name); table.add_row(*values)",
        "signature": "def build_table(headers: list[str], rows: list[tuple]) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.table import Table\n"
            '    t = build_table(["a", "b"], [("1", "2"), ("3", "4")])\n'
            "    assert isinstance(t, Table)\n"
            "    assert len(t.columns) == 2 and len(t.rows) == 2\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.table import Table\n\n"
            "def build_table(headers: list[str], rows: list[tuple]) -> Table:\n"
            "    table = Table()\n"
            "    for h in headers:\n"
            "        table.add_column(h)\n"
            "    for row in rows:\n"
            "        table.add_row(*row)\n"
            "    return table\n"
        ),
    },
    {
        "slug": "02_render_to_string",
        "track": "rich", "difficulty": "easy",
        "title": "Render to a String",
        "tags": ["rich", "console"],
        "description": "Render a given rich renderable to a string (no terminal) using Console with StringIO and width 80.",
        "examples": "render(table) -> str containing the table text",
        "hint": "Console(file=io.StringIO(), width=80, force_terminal=False); console.print(x).",
        "syntax_hint": "from rich.console import Console; import io; buf=io.StringIO()",
        "signature": "def render(renderable) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.text import Text\n"
            "    s = render(Text('hello'))\n"
            "    assert 'hello' in s\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import io\nfrom rich.console import Console\n\n"
            "def render(renderable) -> str:\n"
            "    buf = io.StringIO()\n"
            "    console = Console(file=buf, width=80, force_terminal=False)\n"
            "    console.print(renderable)\n"
            "    return buf.getvalue()\n"
        ),
    },
    {
        "slug": "03_styled_text",
        "track": "rich", "difficulty": "easy",
        "title": "Styled Text",
        "tags": ["rich", "text"],
        "description": "Return a rich.text.Text with the given string styled 'bold red'.",
        "examples": "styled('hi') -> Text with style bold red",
        "hint": "Text(string, style='bold red').",
        "syntax_hint": "from rich.text import Text; Text(s, style='bold red')",
        "signature": "def styled(s: str) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.text import Text\n"
            "    t = styled('hi')\n"
            "    assert isinstance(t, Text)\n"
            "    assert str(t) == 'hi'\n"
            "    assert 'red' in str(t.style) and 'bold' in str(t.style)\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.text import Text\n\n"
            "def styled(s: str) -> Text:\n"
            "    return Text(s, style='bold red')\n"
        ),
    },
    {
        "slug": "04_panel_wrap",
        "track": "rich", "difficulty": "easy",
        "title": "Wrap in a Panel",
        "tags": ["rich", "panel"],
        "description": "Return a rich.panel.Panel titled with the given title wrapping the given text.",
        "examples": "wrap('body', 'Title') -> Panel",
        "hint": "Panel(text, title=title).",
        "syntax_hint": "from rich.panel import Panel; Panel(text, title=title)",
        "signature": "def wrap(text: str, title: str) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.panel import Panel\n"
            "    p = wrap('body', 'Title')\n"
            "    assert isinstance(p, Panel)\n"
            "    assert p.title == 'Title'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.panel import Panel\n\n"
            "def wrap(text: str, title: str) -> Panel:\n"
            "    return Panel(text, title=title)\n"
        ),
    },
    {
        "slug": "05_tree_build",
        "track": "rich", "difficulty": "medium",
        "title": "Build a Tree",
        "tags": ["rich", "tree"],
        "description": "Return a rich.tree.Tree with root label 'root' and one child per item in items.",
        "examples": "tree(['a','b']) -> Tree with 2 children",
        "hint": "tree.add(label) adds a child branch.",
        "syntax_hint": "from rich.tree import Tree; t = Tree('root'); for x in items: t.add(x)",
        "signature": "def tree(items: list[str]) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.tree import Tree\n"
            "    t = tree(['a', 'b'])\n"
            "    assert isinstance(t, Tree)\n"
            "    assert len(t.children) == 2\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.tree import Tree\n\n"
            "def tree(items: list[str]) -> Tree:\n"
            "    t = Tree('root')\n"
            "    for x in items:\n"
            "        t.add(x)\n"
            "    return t\n"
        ),
    },
    {
        "slug": "06_columns_split",
        "track": "rich", "difficulty": "easy",
        "title": "Join with Columns",
        "tags": ["rich", "columns"],
        "description": "Return a rich.columns.Columns containing one rich.text.Text per given string.",
        "examples": "columns(['a','b']) -> Columns with 2 renderables",
        "hint": "Columns([Text(s) for s in items]).",
        "syntax_hint": "from rich.columns import Columns; Columns([Text(s) for s in items])",
        "signature": "def columns(items: list[str]) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.columns import Columns\n"
            "    c = columns(['a', 'b'])\n"
            "    assert isinstance(c, Columns)\n"
            "    assert len(c.renderables) == 2\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.columns import Columns\nfrom rich.text import Text\n\n"
            "def columns(items: list[str]) -> Columns:\n"
            "    return Columns([Text(s) for s in items])\n"
        ),
    },
    {
        "slug": "07_syntax_highlight",
        "track": "rich", "difficulty": "medium",
        "title": "Syntax Block",
        "tags": ["rich", "syntax"],
        "description": "Return a rich.syntax.Syntax block for the given Python code string with background disabled.",
        "examples": "code_block('x = 1') -> Syntax",
        "hint": "Syntax(code, 'python', background='default').",
        "syntax_hint": "from rich.syntax import Syntax; Syntax(code, 'python')",
        "signature": "def code_block(code: str) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.syntax import Syntax\n"
            "    s = code_block('x = 1')\n"
            "    assert isinstance(s, Syntax)\n"
            "    assert s.code == 'x = 1'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.syntax import Syntax\n\n"
            "def code_block(code: str) -> Syntax:\n"
            "    return Syntax(code, 'python')\n"
        ),
    },
    {
        "slug": "08_progress_tracks",
        "track": "rich", "difficulty": "hard",
        "title": "Progress Tracks",
        "tags": ["rich", "progress"],
        "description": "Return a rich.progress.Progress configured with a spinner, a bar, and percentage columns (no transient).",
        "examples": "make_progress() -> Progress",
        "hint": "Use Progress with SpinnerColumn, BarColumn, TextColumn, TaskProgressColumn.",
        "syntax_hint": "from rich.progress import Progress, SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn",
        "signature": "def make_progress() -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.progress import Progress\n"
            "    p = make_progress()\n"
            "    assert isinstance(p, Progress)\n"
            "    assert p.live.transient is False\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.progress import (\n"
            "    Progress, SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn,\n)\n\n"
            "def make_progress() -> Progress:\n"
            "    return Progress(\n"
            "        SpinnerColumn(),\n"
            "        TextColumn('[progress.description]{task.description}'),\n"
            "        BarColumn(),\n"
            "        TaskProgressColumn(),\n"
            "        transient=False,\n"
            "    )\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_rich_intro",
        "track": "rich", "difficulty": "easy",
        "title": "Rich Output",
        "tags": ["rich", "console"],
        "exercise": "content/problems/rich/easy/01_build_table.py",
        "body": (
            "# Rich Output\n\n"
            "The `rich` library renders styled terminal output: tables, panels, trees.\n\n"
            "## Tables\n\n"
            "```python\nfrom rich.table import Table\ntable = Table()\n"
            "table.add_column('Name')\ntable.add_row('Alice')\nprint(table)\n```\n\n"
            "Tables expose `.columns` and `.rows`, so you can test them without rendering. "
            "Use `Console(file=io.StringIO(), width=80)` to capture output as a string."
        ),
    },
]
