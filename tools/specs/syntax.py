"""Python syntax problem specs."""

PROBLEMS = [
    {
        "slug": "01_list_comprehension_evens",
        "track": "syntax", "difficulty": "easy",
        "title": "List Comprehension - Evens",
        "tags": ["comprehension", "list"],
        "description": "Return a list of the even numbers from the input list, squared, using a list comprehension.",
        "examples": "even_squares([1,2,3,4]) -> [4,16]",
        "hint": "Filter with `if x % 2 == 0` inside the comprehension, then square.",
        "syntax_hint": "[x * x for x in numbers if x % 2 == 0]",
        "signature": "def even_squares(numbers: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert even_squares([1, 2, 3, 4]) == [4, 16]\n"
            "    assert even_squares([2, 4]) == [4, 16]\n"
            "    assert even_squares([1, 3, 5]) == []\n"
            "    assert even_squares([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def even_squares(numbers: list[int]) -> list[int]:\n"
            "    return [x * x for x in numbers if x % 2 == 0]\n"
        ),
    },
    {
        "slug": "02_dict_comprehension_lengths",
        "track": "syntax", "difficulty": "easy",
        "title": "Dict Comprehension - Lengths",
        "tags": ["comprehension", "dict"],
        "description": "Return a dict mapping each word to its length, using a dict comprehension.",
        "examples": 'lengths(["hi","there"]) -> {"hi":2,"there":5}',
        "hint": "{word: len(word) for word in words}",
        "syntax_hint": "dict comprehension has the form {key: value for ...}.",
        "signature": "def lengths(words: list[str]) -> dict[str, int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert lengths(["hi", "there"]) == {"hi": 2, "there": 5}\n'
            "    assert lengths([]) == {}\n"
            '    assert lengths(["x"]) == {"x": 1}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def lengths(words: list[str]) -> dict[str, int]:\n"
            "    return {w: len(w) for w in words}\n"
        ),
    },
    {
        "slug": "03_enumerate_line_numbers",
        "track": "syntax", "difficulty": "easy",
        "title": "Enumerate - Line Numbers",
        "tags": ["enumerate", "string"],
        "description": "Given a list of lines, return a list of strings like '1: line' using enumerate starting at 1.",
        "examples": 'number_lines(["a","b"]) -> ["1: a","2: b"]',
        "hint": "enumerate(lines, start=1) yields (index, value).",
        "syntax_hint": 'f"{i}: {line}" for i, line in enumerate(lines, start=1)',
        "signature": "def number_lines(lines: list[str]) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert number_lines(["a", "b"]) == ["1: a", "2: b"]\n'
            "    assert number_lines([]) == []\n"
            '    assert number_lines(["only"]) == ["1: only"]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def number_lines(lines: list[str]) -> list[str]:\n"
            '    return [f"{i}: {line}" for i, line in enumerate(lines, start=1)]\n'
        ),
    },
    {
        "slug": "04_zip_pairwise_sums",
        "track": "syntax", "difficulty": "easy",
        "title": "Zip - Pairwise Sums",
        "tags": ["zip"],
        "description": "Given two equal-length lists, return a list of their element-wise sums using zip.",
        "examples": "pairwise_sum([1,2,3],[10,20,30]) -> [11,22,33]",
        "hint": "zip(a, b) yields (a_i, b_i) pairs.",
        "syntax_hint": "[a + b for a, b in zip(xs, ys)]",
        "signature": "def pairwise_sum(xs: list[int], ys: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert pairwise_sum([1, 2, 3], [10, 20, 30]) == [11, 22, 33]\n"
            "    assert pairwise_sum([], []) == []\n"
            "    assert pairwise_sum([1], [2]) == [3]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def pairwise_sum(xs: list[int], ys: list[int]) -> list[int]:\n"
            "    return [a + b for a, b in zip(xs, ys)]\n"
        ),
    },
    {
        "slug": "05_unpacking_head_tail",
        "track": "syntax", "difficulty": "easy",
        "title": "Unpacking - Head and Tail",
        "tags": ["unpacking"],
        "description": "Return (first, rest) where rest is a list of the remaining elements, using unpacking.",
        "examples": "head_tail([1,2,3,4]) -> (1, [2,3,4])",
        "hint": "first, *rest = items unpacks the head from the tail.",
        "syntax_hint": "first, *rest = items; return first, rest",
        "signature": "def head_tail(items: list) -> tuple:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert head_tail([1, 2, 3, 4]) == (1, [2, 3, 4])\n"
            "    assert head_tail(['a']) == ('a', [])\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def head_tail(items: list) -> tuple:\n"
            "    first, *rest = items\n"
            "    return first, rest\n"
        ),
    },
    {
        "slug": "06_walrus_read_until_blank",
        "track": "syntax", "difficulty": "easy",
        "title": "Walrus Operator - Read Until Blank",
        "tags": ["walrus"],
        "description": "Read lines from the iterator until a blank line appears; return the non-blank lines. Use the walrus operator.",
        "examples": 'read_until_blank(iter(["a","b","","c"])) -> ["a","b"]',
        "hint": "while (line := next(it, None)) is not None: stop on empty string.",
        "syntax_hint": "while (line := next(it, None)) is not None: if line == '': break",
        "signature": "def read_until_blank(it) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert read_until_blank(iter(["a", "b", "", "c"])) == ["a", "b"]\n'
            '    assert read_until_blank(iter(["x", "y"])) == ["x", "y"]\n'
            '    assert read_until_blank(iter([])) == []\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def read_until_blank(it) -> list[str]:\n"
            "    result = []\n"
            "    while (line := next(it, None)) is not None:\n"
            "        if line == '':\n"
            "            break\n"
            "        result.append(line)\n"
            "    return result\n"
        ),
    },
    {
        "slug": "07_defaultdict_groupby",
        "track": "syntax", "difficulty": "easy",
        "title": "defaultdict - Group By Length",
        "tags": ["collections"],
        "description": "Group words by their length into a dict mapping length -> list of words, using collections.defaultdict.",
        "examples": 'group_by_len(["a","bb","c","dd"]) -> {1:["a","c"], 2:["bb","dd"]}',
        "hint": "defaultdict(list) auto-creates empty lists.",
        "syntax_hint": "from collections import defaultdict; d = defaultdict(list); d[len(w)].append(w)",
        "signature": "def group_by_len(words: list[str]) -> dict[int, list[str]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert group_by_len(["a", "bb", "c", "dd"]) == {1: ["a", "c"], 2: ["bb", "dd"]}\n'
            "    assert group_by_len([]) == {}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import defaultdict\n\n"
            "def group_by_len(words: list[str]) -> dict[int, list[str]]:\n"
            "    d: dict[int, list[str]] = defaultdict(list)\n"
            "    for w in words:\n"
            "        d[len(w)].append(w)\n"
            "    return dict(d)\n"
        ),
    },
    {
        "slug": "08_counter_top_words",
        "track": "syntax", "difficulty": "easy",
        "title": "Counter - Top Words",
        "tags": ["collections"],
        "description": "Return the n most common words (as (word, count) pairs) using collections.Counter.",
        "examples": 'top_words(["a","b","a","c","a","b"], 2) -> [("a",3),("b",2)]',
        "hint": "Counter(words).most_common(n) does exactly this.",
        "syntax_hint": "from collections import Counter; Counter(words).most_common(n)",
        "signature": "def top_words(words: list[str], n: int) -> list[tuple[str, int]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert top_words(["a", "b", "a", "c", "a", "b"], 2) == [("a", 3), ("b", 2)]\n'
            '    assert top_words(["x"], 1) == [("x", 1)]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def top_words(words: list[str], n: int) -> list[tuple[str, int]]:\n"
            "    return Counter(words).most_common(n)\n"
        ),
    },
    {
        "slug": "09_decorator_shout",
        "track": "syntax", "difficulty": "medium",
        "title": "Decorator - Shout",
        "tags": ["decorator"],
        "description": "Write a decorator `shout` that uppercases string return values. Non-string returns pass through unchanged.",
        "examples": 'shout(greet)("eli") -> "HELLO ELI"',
        "hint": "Define wrapper(*args, **kwargs); call func, then .upper() if the result is a str.",
        "syntax_hint": "functools.wraps(func) keeps the wrapped function's metadata.",
        "signature": "def shout(func):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    @shout\n"
            "    def greet(name: str) -> str:\n"
            '        return f"hello {name}"\n'
            "    @shout\n"
            "    def add(a: int, b: int) -> int:\n"
            "        return a + b\n"
            '    assert greet("eli") == "HELLO ELI"\n'
            '    assert greet("world") == "HELLO WORLD"\n'
            "    assert add(2, 3) == 5\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import functools\n\n"
            "def shout(func):\n"
            "    @functools.wraps(func)\n"
            "    def wrapper(*args, **kwargs):\n"
            "        result = func(*args, **kwargs)\n"
            "        if isinstance(result, str):\n"
            "            return result.upper()\n"
            "        return result\n"
            "    return wrapper\n"
        ),
    },
    {
        "slug": "10_dataclass_point",
        "track": "syntax", "difficulty": "medium",
        "title": "Dataclass - Point",
        "tags": ["dataclass"],
        "description": "Define a Point dataclass with x and y, plus a method moved(dx, dy) returning a new Point.",
        "examples": "Point(1,2).moved(3,4) -> Point(4,6)",
        "hint": "@dataclass(frozen=True) gives you __init__ and __eq__ for free.",
        "syntax_hint": "from dataclasses import dataclass; @dataclass(frozen=True)",
        "signature": (
            "from dataclasses import dataclass\n\n"
            "@dataclass(frozen=True)\n"
            "class Point:\n"
            "    pass"
        ),
        "tests": (
            "def run_tests() -> None:\n"
            "    p = Point(1, 2)\n"
            "    assert p.x == 1 and p.y == 2\n"
            "    q = p.moved(3, 4)\n"
            "    assert q == Point(4, 6)\n"
            "    assert p == Point(1, 2)\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from dataclasses import dataclass\n\n"
            "@dataclass(frozen=True)\n"
            "class Point:\n"
            "    x: int\n"
            "    y: int\n"
            "\n"
            "    def moved(self, dx: int, dy: int) -> 'Point':\n"
            "        return Point(self.x + dx, self.y + dy)\n"
        ),
    },
    {
        "slug": "11_match_http_status",
        "track": "syntax", "difficulty": "easy",
        "title": "Match - HTTP Status",
        "tags": ["match"],
        "description": "Use a match statement to return 'ok' for 200, 'created' for 201, 'not found' for 404, 'error' otherwise.",
        "examples": "describe(200) -> 'ok'\ndescribe(500) -> 'error'",
        "hint": "match status: case 200: ... case 404: ... case _: ...",
        "syntax_hint": "match/case with a default case _ catches everything else.",
        "signature": "def describe(status: int) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert describe(200) == 'ok'\n"
            "    assert describe(201) == 'created'\n"
            "    assert describe(404) == 'not found'\n"
            "    assert describe(500) == 'error'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def describe(status: int) -> str:\n"
            "    match status:\n"
            "        case 200:\n"
            "            return 'ok'\n"
            "        case 201:\n"
            "            return 'created'\n"
            "        case 404:\n"
            "            return 'not found'\n"
            "        case _:\n"
            "            return 'error'\n"
        ),
    },
    {
        "slug": "12_generator_batches",
        "track": "syntax", "difficulty": "medium",
        "title": "Generator - Batches",
        "tags": ["generator"],
        "description": "Write a generator that yields successive sublists of size n from a list (the last batch may be smaller).",
        "examples": "list(batches([1,2,3,4,5], 2)) -> [[1,2],[3,4],[5]]",
        "hint": "yield items[i:i+n] in a loop; slicing handles the remainder.",
        "syntax_hint": "for i in range(0, len(items), n): yield items[i:i+n]",
        "signature": "def batches(items: list, n: int):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert list(batches([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]\n"
            "    assert list(batches([1, 2], 5)) == [[1, 2]]\n"
            "    assert list(batches([], 2)) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def batches(items: list, n: int):\n"
            "    for i in range(0, len(items), n):\n"
            "        yield items[i:i + n]\n"
        ),
    },
    {
        "slug": "13_fstring_price_table",
        "track": "syntax", "difficulty": "easy",
        "title": "f-strings - Price Table",
        "tags": ["fstring"],
        "description": "Given a list of (name, price) tuples, return lines like 'apple: $1.20' with two decimals using f-strings.",
        "examples": 'price_table([("apple",1.2)]) -> ["apple: $1.20"]',
        "hint": "f'{name}: ${price:.2f}' formats to two decimals.",
        "syntax_hint": "f'{name}: ${price:.2f}'",
        "signature": "def price_table(rows: list[tuple[str, float]]) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert price_table([("apple", 1.2)]) == ["apple: $1.20"]\n'
            '    assert price_table([("x", 0), ("y", 5)]) == ["x: $0.00", "y: $5.00"]\n'
            "    assert price_table([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def price_table(rows: list[tuple[str, float]]) -> list[str]:\n"
            "    return [f'{name}: ${price:.2f}' for name, price in rows]\n"
        ),
    },
    {
        "slug": "14_slice_every_nth",
        "track": "syntax", "difficulty": "easy",
        "title": "Slicing - Every Nth",
        "tags": ["slicing"],
        "description": "Return every nth element of a list using slicing (0-indexed, starting at index 0).",
        "examples": "every_nth([0,1,2,3,4,5], 2) -> [0,2,4]",
        "hint": "lst[::n] steps by n.",
        "syntax_hint": "lst[::n]",
        "signature": "def every_nth(lst: list, n: int) -> list:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert every_nth([0, 1, 2, 3, 4, 5], 2) == [0, 2, 4]\n"
            "    assert every_nth([0, 1, 2, 3, 4, 5], 3) == [0, 3]\n"
            "    assert every_nth([1], 1) == [1]\n"
            "    assert every_nth([], 2) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def every_nth(lst: list, n: int) -> list:\n"
            "    return lst[::n]\n"
        ),
    },
    {
        "slug": "15_args_kwargs_greet",
        "track": "syntax", "difficulty": "easy",
        "title": "*args and **kwargs - Greet",
        "tags": ["args", "kwargs"],
        "description": "Write greet(greeting, *names, **punctuation) that returns 'Hi, a and b!' where '!' comes from the punct keyword.",
        "examples": 'greet("Hi","a","b",punct="!") -> "Hi, a and b!"',
        "hint": "*names collects extra positional args; **punctuation collects keyword args.",
        "syntax_hint": '" and ".join(names); punct = punctuation.get("punct", "")',
        "signature": "def greet(greeting: str, *names, **punctuation) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert greet("Hi", "a", "b", punct="!") == "Hi, a and b!"\n'
            '    assert greet("Hey", "solo") == "Hey, solo"\n'
            '    assert greet("Yo", "a", "b", "c", punct="?") == "Yo, a and b and c?"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def greet(greeting: str, *names, **punctuation) -> str:\n"
            "    punct = punctuation.get('punct', '')\n"
            "    return f\"{greeting}, {' and '.join(names)}{punct}\"\n"
        ),
    },
    {
        "slug": "16_set_comprehension_vowels",
        "track": "syntax", "difficulty": "easy",
        "title": "Set Comprehension - Vowels",
        "tags": ["comprehension", "set"],
        "description": "Return the set of vowels present in a string (case-insensitive), using a set comprehension.",
        "examples": 'vowels("Hello World") -> {"e","o"}',
        "hint": "{ch for ch in text.lower() if ch in 'aeiou'}",
        "syntax_hint": "set comprehension: {expr for ... if ...}",
        "signature": "def vowels(text: str) -> set[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert vowels("Hello World") == {"e", "o"}\n'
            '    assert vowels("sky") == set()\n'
            '    assert vowels("AEI") == {"a", "e", "i"}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def vowels(text: str) -> set[str]:\n"
            "    return {ch for ch in text.lower() if ch in 'aeiou'}\n"
        ),
    },
    {
        "slug": "17_lru_cache_fib",
        "track": "syntax", "difficulty": "medium",
        "title": "functools.lru_cache - Fibonacci",
        "tags": ["cache", "recursion"],
        "description": "Implement a recursive fibonacci using @functools.lru_cache to memoize.",
        "examples": "fib(10) -> 55",
        "hint": "@lru_cache(None) on the recursive function caches results.",
        "syntax_hint": "from functools import lru_cache; @lru_cache(None)",
        "signature": "def fib(n: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert fib(0) == 0\n"
            "    assert fib(1) == 1\n"
            "    assert fib(10) == 55\n"
            "    assert fib(20) == 6765\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from functools import lru_cache\n\n"
            "@lru_cache(None)\n"
            "def fib(n: int) -> int:\n"
            "    if n < 2:\n"
            "        return n\n"
            "    return fib(n - 1) + fib(n - 2)\n"
        ),
    },
    {
        "slug": "18_any_all_check",
        "track": "syntax", "difficulty": "easy",
        "title": "any() and all() - Checks",
        "tags": ["any", "all"],
        "description": "Return (has_negatives, all_positive): whether any number is negative, and whether all are strictly positive.",
        "examples": "check([1,2,-3]) -> (True, False)\ncheck([1,2]) -> (False, True)",
        "hint": "any(x < 0 for x in nums); all(x > 0 for x in nums).",
        "syntax_hint": "any() short-circuits on True; all() short-circuits on False.",
        "signature": "def check(nums: list[int]) -> tuple[bool, bool]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert check([1, 2, -3]) == (True, False)\n"
            "    assert check([1, 2]) == (False, True)\n"
            "    assert check([]) == (False, True)\n"
            "    assert check([-1]) == (True, False)\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def check(nums: list[int]) -> tuple[bool, bool]:\n"
            "    return any(x < 0 for x in nums), all(x > 0 for x in nums)\n"
        ),
    },
    {
        "slug": "19_sorted_key",
        "track": "syntax", "difficulty": "easy",
        "title": "sorted() with key",
        "tags": ["sorted"],
        "description": "Sort a list of strings by length, then alphabetically, using sorted with a key tuple.",
        "examples": 'sort_len(["bb","a","ccc","b"]) -> ["a","b","bb","ccc"]',
        "hint": "key=lambda s: (len(s), s)",
        "syntax_hint": "sorted(items, key=lambda s: (len(s), s))",
        "signature": "def sort_len(words: list[str]) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert sort_len(["bb", "a", "ccc", "b"]) == ["a", "b", "bb", "ccc"]\n'
            '    assert sort_len(["aaa", "b", "cc"]) == ["b", "cc", "aaa"]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def sort_len(words: list[str]) -> list[str]:\n"
            "    return sorted(words, key=lambda s: (len(s), s))\n"
        ),
    },
    {
        "slug": "20_chain_iterables",
        "track": "syntax", "difficulty": "easy",
        "title": "itertools.chain - Flatten",
        "tags": ["itertools"],
        "description": "Flatten a list of lists into one list using itertools.chain.",
        "examples": "flatten([[1,2],[3],[4,5]]) -> [1,2,3,4,5]",
        "hint": "itertools.chain.from_iterable chains an iterable of iterables.",
        "syntax_hint": "from itertools import chain; list(chain.from_iterable(items))",
        "signature": "def flatten(items: list[list]) -> list:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]\n"
            "    assert flatten([]) == []\n"
            "    assert flatten([[], [1]]) == [1]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from itertools import chain\n\n"
            "def flatten(items: list[list]) -> list:\n"
            "    return list(chain.from_iterable(items))\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_list_comprehensions",
        "track": "syntax", "difficulty": "easy",
        "title": "List Comprehensions",
        "tags": ["comprehension", "list"],
        "exercise": "content/problems/syntax/easy/01_list_comprehension_evens.py",
        "body": (
            "# List comprehensions\n\n"
            "A list comprehension builds a list in one expression:\n\n"
            "```python\n[expression for item in iterable if condition]\n```\n\n"
            "## Filter + transform\n\n"
            "```python\n[x * x for x in numbers if x % 2 == 0]\n```\n\n"
            "Read it left to right: *the output value*, *the loop*, *the filter*.\n\n"
            "Comprehensions shine for pure transforms; reach for a loop when the body "
            "gets long or needs side effects."
        ),
    },
    {
        "slug": "02_unpacking",
        "track": "syntax", "difficulty": "easy",
        "title": "Iterable Unpacking",
        "tags": ["unpacking"],
        "exercise": "content/problems/syntax/easy/05_unpacking_head_tail.py",
        "body": (
            "# Iterable unpacking\n\n"
            "Python can pull items apart in one statement:\n\n"
            "```python\nfirst, *rest = items\na, b, *c = range(5)  # a=0, b=1, c=[2,3,4]\n```\n\n"
            "The star collects the remainder into a list. It also works in `for` loops "
            "and function calls."
        ),
    },
    {
        "slug": "03_decorators",
        "track": "syntax", "difficulty": "medium",
        "title": "Decorators",
        "tags": ["decorator"],
        "exercise": "content/problems/syntax/medium/09_decorator_shout.py",
        "body": (
            "# Decorators\n\n"
            "A decorator wraps a function to add behavior without changing its source.\n\n"
            "```python\nimport functools\n\ndef shout(func):\n"
            "    @functools.wraps(func)\n"
            "    def wrapper(*args, **kwargs):\n"
            "        result = func(*args, **kwargs)\n"
            "        return result.upper() if isinstance(result, str) else result\n"
            "    return wrapper\n```\n\n"
            "`@functools.wraps` preserves the original function's name and docstring. "
            "Decorators run at *definition* time, not call time."
        ),
    },
]
