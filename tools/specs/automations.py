"""Automations problem specs (local scripts, files, data tasks)."""

PROBLEMS = [
    {
        "slug": "01_word_frequency",
        "track": "automations", "difficulty": "easy",
        "title": "Word Frequency",
        "tags": ["collections", "string"],
        "description": "Given a string of whitespace-separated words, return a dict mapping each lowercase word to its count.",
        "examples": 'word_counts("a b a") -> {"a":2,"b":1}',
        "hint": "collections.Counter counts an iterable of words.",
        "syntax_hint": "text.lower().split() lowercases and splits on any whitespace.",
        "signature": "def word_counts(text: str) -> dict[str, int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert word_counts("a b a") == {"a": 2, "b": 1}\n'
            '    assert word_counts("Hello hello") == {"hello": 2}\n'
            '    assert word_counts("") == {}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def word_counts(text: str) -> dict[str, int]:\n"
            "    return dict(Counter(text.lower().split()))\n"
        ),
    },
    {
        "slug": "02_extract_emails",
        "track": "automations", "difficulty": "easy",
        "title": "Extract Emails",
        "tags": ["regex"],
        "description": "Return all unique email-like addresses found in a text, in order of first appearance.",
        "examples": 'extract_emails("a@x.com b@y.com a@x.com") -> ["a@x.com","b@y.com"]',
        "hint": "re.findall with a simple email pattern; dedupe keeping order.",
        "syntax_hint": r"pattern r'[\w.+-]+@[\w-]+\.[\w.-]+'",
        "signature": "def extract_emails(text: str) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert extract_emails("a@x.com b@y.com a@x.com") == ["a@x.com", "b@y.com"]\n'
            '    assert extract_emails("no emails here") == []\n'
            '    assert extract_emails("reach eli.test@site.io") == ["eli.test@site.io"]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import re\n\n"
            "def extract_emails(text: str) -> list[str]:\n"
            "    seen: set[str] = set()\n"
            "    result: list[str] = []\n"
            "    for m in re.findall(r\"[\\w.+-]+@[\\w-]+\\.[\\w.-]+\", text):\n"
            "        if m not in seen:\n"
            "            seen.add(m)\n"
            "            result.append(m)\n"
            "    return result\n"
        ),
    },
    {
        "slug": "03_filename_cleaner",
        "track": "automations", "difficulty": "easy",
        "title": "Filename Cleaner",
        "tags": ["regex", "string"],
        "description": "Turn a messy title into a slug: lowercase, spaces to dashes, strip non-alphanumeric except dashes.",
        "examples": 'slugify("Hello, World!") -> "hello-world"',
        "hint": "re.sub(r'[^a-z0-9-]', '', ...) after replacing spaces.",
        "syntax_hint": "re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')",
        "signature": "def slugify(text: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert slugify("Hello, World!") == "hello-world"\n'
            '    assert slugify("  Py   Prac Lab  ") == "py-prac-lab"\n'
            '    assert slugify("ok") == "ok"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import re\n\n"
            "def slugify(text: str) -> str:\n"
            "    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')\n"
        ),
    },
    {
        "slug": "04_csv_expense_summary",
        "track": "automations", "difficulty": "easy",
        "title": "CSV Expense Summary",
        "tags": ["csv", "io"],
        "description": "Given CSV text with columns 'item,amount', return the total of the amounts as a float.",
        "examples": 'total_expenses("item,amount\\nA,1.5\\nB,2.5") -> 4.0',
        "hint": "csv.DictReader over an io.StringIO of the text.",
        "syntax_hint": "import csv, io; for row in csv.DictReader(io.StringIO(text)): sum += float(row['amount'])",
        "signature": "def total_expenses(text: str) -> float:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert total_expenses("item,amount\\nA,1.5\\nB,2.5") == 4.0\n'
            '    assert total_expenses("item,amount\\nX,10") == 10.0\n'
            '    assert total_expenses("item,amount\\n") == 0.0\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import csv\nimport io\n\n"
            "def total_expenses(text: str) -> float:\n"
            "    total = 0.0\n"
            "    for row in csv.DictReader(io.StringIO(text)):\n"
            "        total += float(row['amount'])\n"
            "    return total\n"
        ),
    },
    {
        "slug": "05_log_error_counter",
        "track": "automations", "difficulty": "easy",
        "title": "Log Error Counter",
        "tags": ["string"],
        "description": "Given multi-line log text, return the number of lines containing the word ERROR.",
        "examples": 'count_errors("INFO ok\\nERROR bad\\nERROR worse") -> 2',
        "hint": "Split into lines and count those containing 'ERROR'.",
        "syntax_hint": "sum('ERROR' in line for line in text.splitlines())",
        "signature": "def count_errors(text: str) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert count_errors("INFO ok\\nERROR bad\\nERROR worse") == 2\n'
            '    assert count_errors("all good") == 0\n'
            '    assert count_errors("") == 0\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def count_errors(text: str) -> int:\n"
            "    return sum('ERROR' in line for line in text.splitlines())\n"
        ),
    },
    {
        "slug": "06_directory_size",
        "track": "automations", "difficulty": "easy",
        "title": "Directory Size",
        "tags": ["pathlib"],
        "description": "Given a directory Path, return the total size in bytes of all files recursively.",
        "examples": "dir_size(path) -> int",
        "hint": "path.rglob('*') yields all paths; sum file sizes.",
        "syntax_hint": "sum(p.stat().st_size for p in d.rglob('*') if p.is_file())",
        "signature": "def dir_size(d) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import tempfile, os\n"
            "    from pathlib import Path\n"
            "    with tempfile.TemporaryDirectory() as td:\n"
            "        root = Path(td)\n"
            "        (root / 'a.txt').write_text('12')  # 2 bytes\n"
            "        sub = root / 'sub'\n"
            "        sub.mkdir()\n"
            "        (sub / 'b.txt').write_text('abc')  # 3 bytes\n"
            "        assert dir_size(root) == 5\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def dir_size(d) -> int:\n"
            "    from pathlib import Path\n"
            "    p = Path(d)\n"
            "    return sum(f.stat().st_size for f in p.rglob('*') if f.is_file())\n"
        ),
    },
    {
        "slug": "07_find_duplicate_lines",
        "track": "automations", "difficulty": "medium",
        "title": "Find Duplicate Lines",
        "tags": ["set", "io"],
        "description": "Return the set of lines that appear more than once in a multi-line string (stripped).",
        "examples": 'dup_lines("a\\nb\\na\\nc") -> {"a"}',
        "hint": "Count lines; keep those with count > 1.",
        "syntax_hint": "from collections import Counter; {l for l, c in Counter(lines).items() if c > 1}",
        "signature": "def dup_lines(text: str) -> set[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert dup_lines("a\\nb\\na\\nc") == {"a"}\n'
            '    assert dup_lines("one\\ntwo") == set()\n'
            '    assert dup_lines("x\\nx\\ny\\ny") == {"x", "y"}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def dup_lines(text: str) -> set[str]:\n"
            "    counts = Counter(text.splitlines())\n"
            "    return {line for line, c in counts.items() if c > 1}\n"
        ),
    },
    {
        "slug": "08_key_value_parser",
        "track": "automations", "difficulty": "easy",
        "title": "Key-Value Parser",
        "tags": ["string"],
        "description": "Parse lines 'key=value' into a dict. Skip blank lines and lines without '='.",
        "examples": 'parse_kv("a=1\\nb=2\\n# no") -> {"a":"1","b":"2"}',
        "hint": "line.split('=', 1) gives key and value.",
        "syntax_hint": "if '=' in line: k, v = line.split('=', 1); d[k.strip()] = v.strip()",
        "signature": "def parse_kv(text: str) -> dict[str, str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert parse_kv("a=1\\nb=2\\n# no") == {"a": "1", "b": "2"}\n'
            '    assert parse_kv("name = eli") == {"name": "eli"}\n'
            '    assert parse_kv("") == {}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def parse_kv(text: str) -> dict[str, str]:\n"
            "    out = {}\n"
            "    for line in text.splitlines():\n"
            "        if '=' in line:\n"
            "            k, v = line.split('=', 1)\n"
            "            out[k.strip()] = v.strip()\n"
            "    return out\n"
        ),
    },
    {
        "slug": "09_markdown_headings",
        "track": "automations", "difficulty": "easy",
        "title": "Markdown Headings",
        "tags": ["regex", "string"],
        "description": "Return a list of heading texts (without the leading # marks) from a markdown string.",
        "examples": 'headings("# Title\\n## Sub") -> ["Title","Sub"]',
        "hint": "Match lines starting with one or more # then a space.",
        "syntax_hint": r"re.findall(r'^#+\s+(.+)$', text, re.MULTILINE)",
        "signature": "def headings(text: str) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert headings("# Title\\n## Sub") == ["Title", "Sub"]\n'
            '    assert headings("no headings") == []\n'
            '    assert headings("### Deep") == ["Deep"]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import re\n\n"
            "def headings(text: str) -> list[str]:\n"
            "    return re.findall(r'^#+\\s+(.+)$', text, re.MULTILINE)\n"
        ),
    },
    {
        "slug": "10_extension_grouper",
        "track": "automations", "difficulty": "easy",
        "title": "Extension Grouper",
        "tags": ["pathlib", "collections"],
        "description": "Given a list of filenames, group them by file extension into a dict ext -> list of names.",
        "examples": 'group_ext(["a.txt","b.txt","c.md"]) -> {"txt":["a.txt","b.txt"],"md":["c.md"]}',
        "hint": "Path(name).suffix gives the extension.",
        "syntax_hint": "from pathlib import Path; ext = Path(name).suffix",
        "signature": "def group_ext(names: list[str]) -> dict[str, list[str]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert group_ext(["a.txt", "b.txt", "c.md"]) == {"txt": ["a.txt", "b.txt"], "md": ["c.md"]}\n'
            "    assert group_ext([]) == {}\n"
            '    assert group_ext(["noext"]) == {"": ["noext"]}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from pathlib import Path\nfrom collections import defaultdict\n\n"
            "def group_ext(names: list[str]) -> dict[str, list[str]]:\n"
            "    d: dict[str, list[str]] = defaultdict(list)\n"
            "    for n in names:\n"
            "        d[Path(n).suffix.lstrip('.')].append(n)\n"
            "    return dict(d)\n"
        ),
    },
    {
        "slug": "11_truncate_preview",
        "track": "automations", "difficulty": "easy",
        "title": "Truncate Preview",
        "tags": ["string"],
        "description": "Return a one-line preview of text: collapse whitespace and truncate to max chars, adding '...' if cut.",
        "examples": 'preview("hello   world", 8) -> "hello..."',
        "hint": "' '.join(text.split()) collapses all whitespace.",
        "syntax_hint": "if len(s) > n: s = s[:n-3] + '...'",
        "signature": "def preview(text: str, n: int) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert preview("hello   world", 8) == "hello..."\n'
            '    assert preview("hi", 10) == "hi"\n'
            '    assert preview("abcdefgh", 5) == "ab..."\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def preview(text: str, n: int) -> str:\n"
            "    s = ' '.join(text.split())\n"
            "    if len(s) <= n:\n"
            "        return s\n"
            "    return s[:max(0, n - 3)] + '...'\n"
        ),
    },
    {
        "slug": "12_backup_plan",
        "track": "automations", "difficulty": "medium",
        "title": "Backup Plan",
        "tags": ["pathlib", "logic"],
        "description": "Given a list of file paths and a backup dir, return a list of (source, dest) pairs where dest is backup_dir / source.name with a '.bak' suffix appended.",
        "examples": "backup_plan([Path('a.txt')], Path('bk')) -> [(Path('a.txt'), Path('bk/a.txt.bak'))]",
        "hint": "dest = backup_dir / (p.name + '.bak').",
        "syntax_hint": "backup_dir / (p.name + '.bak')",
        "signature": "def backup_plan(files: list, backup_dir) -> list[tuple]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from pathlib import Path\n"
            "    plan = backup_plan([Path('a.txt'), Path('b.log')], Path('bk'))\n"
            "    assert plan == [(Path('a.txt'), Path('bk/a.txt.bak')), (Path('b.log'), Path('bk/b.log.bak'))]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def backup_plan(files: list, backup_dir) -> list[tuple]:\n"
            "    from pathlib import Path\n"
            "    bd = Path(backup_dir)\n"
            "    return [(p, bd / (p.name + '.bak')) for p in files]\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_pathlib",
        "track": "automations", "difficulty": "easy",
        "title": "pathlib Essentials",
        "tags": ["pathlib", "files"],
        "exercise": "content/problems/automations/easy/10_extension_grouper.py",
        "body": (
            "# pathlib\n\n"
            "`pathlib.Path` is the modern way to work with paths.\n\n"
            "```python\nfrom pathlib import Path\np = Path('docs/readme.md')\n"
            "p.suffix      # '.md'\np.stem       # 'readme'\np.name       # 'readme.md'\n"
            "p.parent     # Path('docs')\np.exists()   # True/False\n```\n\n"
            "Use `p.rglob('*.py')` to walk recursively. Prefer Path arithmetic "
            "(`/`) over string concatenation."
        ),
    },
]
