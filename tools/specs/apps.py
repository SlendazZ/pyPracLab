"""Apps problem specs (small applications, OOP, CLI tools)."""

PROBLEMS = [
    {
        "slug": "01_contact_book",
        "track": "apps", "difficulty": "easy",
        "title": "Contact Book",
        "tags": ["oop"],
        "description": "Implement a ContactBook with add_contact(name, email) and find_contact(name) -> dict or None. find is case-insensitive.",
        "examples": 'book.find("Alice") -> {"name": "Alice", "email": "a@x.com"}',
        "hint": "Store contacts as a list of dicts; lower-case the name when searching.",
        "syntax_hint": "class ContactBook: def __init__(self): self._contacts = []",
        "signature": "class ContactBook:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    book = ContactBook()\n"
            '    book.add_contact("Alice", "a@x.com")\n'
            '    book.add_contact("Bob", "b@x.com")\n'
            '    assert book.find_contact("alice") == {"name": "Alice", "email": "a@x.com"}\n'
            '    assert book.find_contact("BOB") == {"name": "Bob", "email": "b@x.com"}\n'
            '    assert book.find_contact("nobody") is None\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "class ContactBook:\n"
            "    def __init__(self):\n"
            "        self._contacts: list[dict] = []\n"
            "    def add_contact(self, name: str, email: str) -> None:\n"
            "        self._contacts.append({'name': name, 'email': email})\n"
            "    def find_contact(self, name: str):\n"
            "        target = name.lower()\n"
            "        for c in self._contacts:\n"
            "            if c['name'].lower() == target:\n"
            "                return c\n"
            "        return None\n"
        ),
    },
    {
        "slug": "02_todo_list",
        "track": "apps", "difficulty": "easy",
        "title": "Todo List",
        "tags": ["oop"],
        "description": "A TodoList with add(task), complete(task), and pending() -> list of unfinished tasks. Completing an unknown task is a no-op.",
        "examples": "t.pending() after add('a') -> ['a']",
        "hint": "Keep a list of dicts with a 'done' flag.",
        "syntax_hint": "[t['title'] for t in self.items if not t['done']]",
        "signature": "class TodoList:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    t = TodoList()\n"
            "    t.add('a'); t.add('b')\n"
            "    assert t.pending() == ['a', 'b']\n"
            "    t.complete('a')\n"
            "    assert t.pending() == ['b']\n"
            "    t.complete('nope')\n"
            "    assert t.pending() == ['b']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "class TodoList:\n"
            "    def __init__(self):\n"
            "        self.items: list[dict] = []\n"
            "    def add(self, task: str) -> None:\n"
            "        self.items.append({'title': task, 'done': False})\n"
            "    def complete(self, task: str) -> None:\n"
            "        for t in self.items:\n"
            "            if t['title'] == task and not t['done']:\n"
            "                t['done'] = True\n"
            "                return\n"
            "    def pending(self) -> list[str]:\n"
            "        return [t['title'] for t in self.items if not t['done']]\n"
        ),
    },
    {
        "slug": "03_stack_class",
        "track": "apps", "difficulty": "easy",
        "title": "Stack Class",
        "tags": ["oop"],
        "description": "Implement a Stack with push(x), pop() (raise IndexError if empty), and peek().",
        "examples": "s.pop() after push(1) -> 1",
        "hint": "Backed by a list; use append and pop.",
        "syntax_hint": "if not self._data: raise IndexError",
        "signature": "class Stack:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    s = Stack()\n"
            "    s.push(1); s.push(2)\n"
            "    assert s.peek() == 2\n"
            "    assert s.pop() == 2\n"
            "    assert s.pop() == 1\n"
            "    try:\n"
            "        s.pop(); assert False\n"
            "    except IndexError:\n"
            "        pass\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "class Stack:\n"
            "    def __init__(self):\n"
            "        self._data: list = []\n"
            "    def push(self, x) -> None:\n"
            "        self._data.append(x)\n"
            "    def pop(self):\n"
            "        if not self._data:\n"
            "            raise IndexError('pop from empty stack')\n"
            "        return self._data.pop()\n"
            "    def peek(self):\n"
            "        if not self._data:\n"
            "            raise IndexError('peek from empty stack')\n"
            "        return self._data[-1]\n"
        ),
    },
    {
        "slug": "04_cli_arg_parser",
        "track": "apps", "difficulty": "medium",
        "title": "Simple CLI Arg Parser",
        "tags": ["cli"],
        "description": "Parse argv like ['--name','eli','--count','3'] into {'name':'eli','count':'3'}. Support '--flag' (sets True).",
        "examples": "parse(['--name','eli','--verbose']) -> {'name':'eli','verbose':True}",
        "hint": "Walk argv; a '--key value' pair sets the key; a lone '--flag' sets True.",
        "syntax_hint": "if arg.startswith('--'): if next doesn't start with '--': set key=next",
        "signature": "def parse(argv: list[str]) -> dict:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert parse(['--name', 'eli', '--verbose']) == {'name': 'eli', 'verbose': True}\n"
            "    assert parse(['--count', '3']) == {'count': '3'}\n"
            "    assert parse([]) == {}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def parse(argv: list[str]) -> dict:\n"
            "    out = {}\n"
            "    i = 0\n"
            "    while i < len(argv):\n"
            "        arg = argv[i]\n"
            "        if arg.startswith('--'):\n"
            "            key = arg[2:]\n"
            "            if i + 1 < len(argv) and not argv[i + 1].startswith('--'):\n"
            "                out[key] = argv[i + 1]\n"
            "                i += 1\n"
            "            else:\n"
            "                out[key] = True\n"
            "        i += 1\n"
            "    return out\n"
        ),
    },
    {
        "slug": "05_unit_converter",
        "track": "apps", "difficulty": "easy",
        "title": "Unit Converter",
        "tags": ["dict"],
        "description": "Convert a value between units of the same kind using a factor table: convert(100, 'cm', 'm') -> 1.0 where factors store meters-per-unit.",
        "examples": "convert(100, 'cm', 'm') -> 1.0",
        "hint": "value_in_base = value * factor[from]; result = value_in_base / factor[to].",
        "syntax_hint": "factors = {'cm': 0.01, 'm': 1.0, 'km': 1000.0}",
        "signature": "def convert(value: float, frm: str, to: str) -> float:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert abs(convert(100, 'cm', 'm') - 1.0) < 1e-9\n"
            "    assert abs(convert(1, 'km', 'm') - 1000.0) < 1e-9\n"
            "    assert abs(convert(2, 'm', 'm') - 2.0) < 1e-9\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def convert(value: float, frm: str, to: str) -> float:\n"
            "    factors = {'cm': 0.01, 'm': 1.0, 'km': 1000.0}\n"
            "    base = value * factors[frm]\n"
            "    return base / factors[to]\n"
        ),
    },
    {
        "slug": "06_temperature_converter",
        "track": "apps", "difficulty": "easy",
        "title": "Temperature Converter",
        "tags": ["math"],
        "description": "Convert between 'C', 'F', 'K'. Support any pair.",
        "examples": "temp(0, 'C', 'F') -> 32.0\ntemp(0, 'C', 'K') -> 273.15",
        "hint": "Convert to Celsius first, then to the target.",
        "syntax_hint": "if frm == 'F': c = (v - 32) * 5/9",
        "signature": "def temp(value: float, frm: str, to: str) -> float:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert abs(temp(0, 'C', 'F') - 32.0) < 1e-9\n"
            "    assert abs(temp(0, 'C', 'K') - 273.15) < 1e-9\n"
            "    assert abs(temp(32, 'F', 'C') - 0.0) < 1e-9\n"
            "    assert abs(temp(100, 'C', 'C') - 100.0) < 1e-9\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def temp(value: float, frm: str, to: str) -> float:\n"
            "    if frm == 'C':\n"
            "        c = value\n"
            "    elif frm == 'F':\n"
            "        c = (value - 32) * 5 / 9\n"
            "    else:\n"
            "        c = value - 273.15\n"
            "    if to == 'C':\n"
            "        return c\n"
            "    if to == 'F':\n"
            "        return c * 9 / 5 + 32\n"
            "    return c + 273.15\n"
        ),
    },
    {
        "slug": "07_inventory_value",
        "track": "apps", "difficulty": "easy",
        "title": "Inventory Total Value",
        "tags": ["dict"],
        "description": "Given an inventory dict {item: (quantity, unit_price)} return the total value.",
        "examples": "total_value({'a': (2, 5), 'b': (1, 10)}) -> 20",
        "hint": "Sum qty * price for each item.",
        "syntax_hint": "sum(q * p for q, p in inv.values())",
        "signature": "def total_value(inv: dict) -> float:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert total_value({'a': (2, 5), 'b': (1, 10)}) == 20\n"
            "    assert total_value({}) == 0\n"
            "    assert total_value({'x': (3, 2.5)}) == 7.5\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def total_value(inv: dict) -> float:\n"
            "    return sum(q * p for q, p in inv.values())\n"
        ),
    },
    {
        "slug": "08_pomodoro_state",
        "track": "apps", "difficulty": "medium",
        "title": "Pomodoro State Machine",
        "tags": ["state"],
        "description": "A Pomodoro cycles 'work' -> 'break' -> 'work'. Implement tick() that advances and returns the current mode after n ticks of 25 work / 5 break.",
        "examples": "p = Pomodoro(); p.tick() x25 -> 'break'",
        "hint": "Track elapsed minutes; switch modes and reset the counter at the threshold.",
        "syntax_hint": "self.elapsed += 1; if self.elapsed >= self.dur: switch",
        "signature": "class Pomodoro:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    p = Pomodoro()\n"
            "    assert p.mode == 'work'\n"
            "    for _ in range(24):\n"
            "        assert p.tick() == 'work'\n"
            "    assert p.tick() == 'break'\n"
            "    for _ in range(4):\n"
            "        assert p.tick() == 'break'\n"
            "    assert p.tick() == 'work'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "class Pomodoro:\n"
            "    def __init__(self):\n"
            "        self.mode = 'work'\n"
            "        self.elapsed = 0\n"
            "        self.dur = 25\n"
            "    def tick(self) -> str:\n"
            "        self.elapsed += 1\n"
            "        if self.elapsed >= self.dur:\n"
            "            self.mode = 'break' if self.mode == 'work' else 'work'\n"
            "            self.dur = 5 if self.mode == 'break' else 25\n"
            "            self.elapsed = 0\n"
            "        return self.mode\n"
        ),
    },
    {
        "slug": "09_email_validator",
        "track": "apps", "difficulty": "easy",
        "title": "Email Validator",
        "tags": ["regex"],
        "description": "Return True if a string is a plausible email: one '@', a local part, a domain with a dot.",
        "examples": 'is_email("a@b.com") -> True\nis_email("nope") -> False',
        "hint": "A simple regex: local@domain.tld with no spaces.",
        "syntax_hint": r"re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', s)",
        "signature": "def is_email(s: str) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert is_email("a@b.com") is True\n'
            '    assert is_email("eli.test@site.io") is True\n'
            '    assert is_email("nope") is False\n'
            '    assert is_email("a @b.com") is False\n'
            '    assert is_email("a@b") is False\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import re\n\n"
            "def is_email(s: str) -> bool:\n"
            "    return re.match(r'^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$', s) is not None\n"
        ),
    },
    {
        "slug": "10_password_strength",
        "track": "apps", "difficulty": "easy",
        "title": "Password Strength",
        "tags": ["string"],
        "description": "Return 'weak' if length < 8, 'medium' if it has >=8 chars and either upper or digit, 'strong' if it has >=8 chars, an upper, and a digit.",
        "examples": 'strength("abc") -> "weak"\nstrength("Abcdefg1") -> "strong"',
        "hint": "Check length, then any(c.isupper()), any(c.isdigit()).",
        "syntax_hint": "has_upper = any(c.isupper() for c in p)",
        "signature": "def strength(p: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert strength("abc") == "weak"\n'
            '    assert strength("abcdefgh") == "medium"\n'
            '    assert strength("abcdefg1") == "medium"\n'
            '    assert strength("Abcdefg1") == "strong"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def strength(p: str) -> str:\n"
            "    if len(p) < 8:\n"
            "        return 'weak'\n"
            "    has_upper = any(c.isupper() for c in p)\n"
            "    has_digit = any(c.isdigit() for c in p)\n"
            "    if has_upper and has_digit:\n"
            "        return 'strong'\n"
            "    return 'medium'\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_oop_basics",
        "track": "apps", "difficulty": "easy",
        "title": "Classes & State",
        "tags": ["oop"],
        "exercise": "content/problems/apps/easy/02_todo_list.py",
        "body": (
            "# Classes\n\n"
            "A class bundles data and the functions that act on it:\n\n"
            "```python\nclass TodoList:\n    def __init__(self):\n"
            "        self.items = []\n    def add(self, task):\n        self.items.append(task)\n```\n\n"
            "`__init__` sets up state; methods take `self` as the first parameter. "
            "Keep internal state private with a leading underscore by convention."
        ),
    },
]
