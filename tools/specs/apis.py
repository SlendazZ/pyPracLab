"""APIs problem specs (request/response handling, JSON, URLs)."""

PROBLEMS = [
    {
        "slug": "01_parse_json_response",
        "track": "apis", "difficulty": "easy",
        "title": "Parse JSON Response",
        "tags": ["json", "api"],
        "description": "Given a JSON string, parse it and return the value of the 'data' key.",
        "examples": 'get_data(\'{"data": [1, 2, 3]}\') -> [1, 2, 3]',
        "hint": "json.loads turns a JSON string into Python objects.",
        "syntax_hint": "import json; obj = json.loads(text); return obj['data']",
        "signature": "def get_data(text: str):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert get_data(\'{"data": [1, 2, 3]}\') == [1, 2, 3]\n'
            '    assert get_data(\'{"data": {"x": 1}}\') == {"x": 1}\n'
            '    assert get_data(\'{"data": "hi"}\') == "hi"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import json\n\n"
            "def get_data(text: str):\n"
            "    return json.loads(text)['data']\n"
        ),
    },
    {
        "slug": "02_build_query_url",
        "track": "apis", "difficulty": "easy",
        "title": "Build Query URL",
        "tags": ["url", "api"],
        "description": "Given a base URL and a dict of query params, return the full URL with query string. Skip params whose value is None.",
        "examples": 'build_url("https://x.test/api", {"q":"py","page":1}) -> "https://x.test/api?q=py&page=1"',
        "hint": "urllib.parse.urlencode encodes a dict into a query string.",
        "syntax_hint": "f\"{base}?{urlencode(params)}\" ; filter None values first.",
        "signature": "def build_url(base: str, params: dict) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    url = build_url("https://x.test/api", {"q": "py", "page": 1})\n'
            '    assert url == "https://x.test/api?q=py&page=1"\n'
            '    assert build_url("https://x.test/api", {}) == "https://x.test/api"\n'
            '    assert build_url("https://x.test/api", {"q": "py", "n": None}) == "https://x.test/api?q=py"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from urllib.parse import urlencode\n\n"
            "def build_url(base: str, params: dict) -> str:\n"
            "    cleaned = {k: v for k, v in params.items() if v is not None}\n"
            "    if not cleaned:\n"
            "        return base\n"
            "    return f\"{base}?{urlencode(cleaned)}\"\n"
        ),
    },
    {
        "slug": "03_pagination_collector",
        "track": "apis", "difficulty": "medium",
        "title": "Pagination Collector",
        "tags": ["api", "loop"],
        "description": "You have fetch(page) -> {'items': [...], 'total': N} with page size 10. Call fetch for pages 1..N until all items are collected, then return the combined list.",
        "examples": "collect(fetch) -> all items across pages",
        "hint": "Loop page=1,2,... ; stop when len(items) >= total.",
        "syntax_hint": "while len(items) < total: page += 1; items.extend(fetch(page)['items'])",
        "signature": "def collect(fetch) -> list:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    pages = {1: {'items': ['a', 'b'], 'total': 3}, 2: {'items': ['c'], 'total': 3}}\n"
            "    def fetch(page):\n"
            "        return pages[page]\n"
            "    assert collect(fetch) == ['a', 'b', 'c']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def collect(fetch) -> list:\n"
            "    items: list = []\n"
            "    total = None\n"
            "    page = 0\n"
            "    while total is None or len(items) < total:\n"
            "        page += 1\n"
            "        data = fetch(page)\n"
            "        items.extend(data['items'])\n"
            "        total = data['total']\n"
            "    return items\n"
        ),
    },
    {
        "slug": "04_status_class",
        "track": "apis", "difficulty": "easy",
        "title": "HTTP Status Class",
        "tags": ["http"],
        "description": "Given an HTTP status code, return 'success' for 2xx, 'redirect' for 3xx, 'client' for 4xx, 'server' for 5xx, else 'unknown'.",
        "examples": "status_class(200) -> 'success'\nstatus_class(404) -> 'client'",
        "hint": "Integer division by 100 gives the class.",
        "syntax_hint": "code // 100",
        "signature": "def status_class(code: int) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert status_class(200) == 'success'\n"
            "    assert status_class(301) == 'redirect'\n"
            "    assert status_class(404) == 'client'\n"
            "    assert status_class(500) == 'server'\n"
            "    assert status_class(99) == 'unknown'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def status_class(code: int) -> str:\n"
            "    classes = {2: 'success', 3: 'redirect', 4: 'client', 5: 'server'}\n"
            "    return classes.get(code // 100, 'unknown')\n"
        ),
    },
    {
        "slug": "05_flatten_json_keys",
        "track": "apis", "difficulty": "medium",
        "title": "Flatten JSON Keys",
        "tags": ["json", "recursion"],
        "description": "Given a nested dict, return a list of dotted-path keys for every leaf (non-dict) value.",
        "examples": 'leaf_keys({"a":{"b":1},"c":2}) -> ["a.b","c"]',
        "hint": "Recurse with a prefix; append the dotted path when the value is not a dict.",
        "syntax_hint": "if isinstance(v, dict): recurse(prefix + k + '.') else: keys.append(prefix + k)",
        "signature": "def leaf_keys(obj: dict) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert sorted(leaf_keys({"a": {"b": 1}, "c": 2})) == ["a.b", "c"]\n'
            '    assert leaf_keys({}) == []\n'
            '    assert leaf_keys({"x": {"y": {"z": 0}}}) == ["x.y.z"]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def leaf_keys(obj: dict) -> list[str]:\n"
            "    keys: list[str] = []\n"
            "    def walk(node, prefix):\n"
            "        for k, v in node.items():\n"
            "            path = prefix + k\n"
            "            if isinstance(v, dict):\n"
            "                walk(v, path + '.')\n"
            "            else:\n"
            "                keys.append(path)\n"
            "    walk(obj, '')\n"
            "    return keys\n"
        ),
    },
    {
        "slug": "06_rate_limiter",
        "track": "apis", "difficulty": "medium",
        "title": "Simple Rate Limiter",
        "tags": ["time", "api"],
        "description": "Implement allow() on a RateLimiter that returns True only if at most `limit` calls happen per `window` seconds. Use time.monotonic().",
        "examples": "rl = RateLimiter(2, 1.0); rl.allow() x2 -> True, rl.allow() -> False",
        "hint": "Keep timestamps of recent calls; drop those older than the window; compare count.",
        "syntax_hint": "import time; self.calls = []; prune calls older than window",
        "signature": (
            "class RateLimiter:\n"
            "    pass"
        ),
        "tests": (
            "def run_tests() -> None:\n"
            "    import time\n"
            "    rl = RateLimiter(2, 1.0)\n"
            "    assert rl.allow() is True\n"
            "    assert rl.allow() is True\n"
            "    assert rl.allow() is False\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import time\nfrom collections import deque\n\n"
            "class RateLimiter:\n"
            "    def __init__(self, limit: int, window: float):\n"
            "        self.limit = limit\n"
            "        self.window = window\n"
            "        self.calls: deque = deque()\n"
            "\n"
            "    def allow(self) -> bool:\n"
            "        now = time.monotonic()\n"
            "        while self.calls and now - self.calls[0] >= self.window:\n"
            "            self.calls.popleft()\n"
            "        if len(self.calls) >= self.limit:\n"
            "            return False\n"
            "        self.calls.append(now)\n"
            "        return True\n"
        ),
    },
    {
        "slug": "07_retry_on_failure",
        "track": "apis", "difficulty": "easy",
        "title": "Retry On Failure",
        "tags": ["loop", "api"],
        "description": "Call a function up to n times; return the first successful result, or raise the last exception.",
        "examples": "retry(flaky, 3) -> result of first successful call",
        "hint": "try/except in a loop; keep last exception.",
        "syntax_hint": "for attempt in range(n): try: return fn() except Exception as e: last = e",
        "signature": "def retry(fn, n: int):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    calls = {'n': 0}\n"
            "    def flaky():\n"
            "        calls['n'] += 1\n"
            "        if calls['n'] < 3:\n"
            "            raise ValueError('boom')\n"
            "        return 'ok'\n"
            "    assert retry(flaky, 5) == 'ok'\n"
            "    assert calls['n'] == 3\n"
            "    def always():\n"
            "        raise RuntimeError('nope')\n"
            "    try:\n"
            "        retry(always, 2)\n"
            "        assert False\n"
            "    except RuntimeError:\n"
            "        pass\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def retry(fn, n: int):\n"
            "    last = None\n"
            "    for _ in range(n):\n"
            "        try:\n"
            "            return fn()\n"
            "        except Exception as e:\n"
            "            last = e\n"
            "    raise last\n"
        ),
    },
    {
        "slug": "08_base64_decode",
        "track": "apis", "difficulty": "easy",
        "title": "Base64 Decode",
        "tags": ["base64"],
        "description": "Given a base64 string, return the decoded bytes.",
        "examples": "decode('aGk=') -> b'hi'",
        "hint": "base64.b64decode decodes a base64 string.",
        "syntax_hint": "import base64; base64.b64decode(s)",
        "signature": "def decode(s: str) -> bytes:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert decode('aGk=') == b'hi'\n"
            "    assert decode('') == b''\n"
            "    assert decode('d29yaw==') == b'work'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import base64\n\n"
            "def decode(s: str) -> bytes:\n"
            "    return base64.b64decode(s)\n"
        ),
    },
    {
        "slug": "09_merge_paginated",
        "track": "apis", "difficulty": "easy",
        "title": "Merge Paginated Items",
        "tags": ["list"],
        "description": "Given a list of page dicts each with an 'items' list, return one combined list of all items.",
        "examples": "merge_pages([{'items':[1]},{'items':[2,3]}]) -> [1,2,3]",
        "hint": "A nested comprehension or itertools.chain flattens them.",
        "syntax_hint": "[item for page in pages for item in page['items']]",
        "signature": "def merge_pages(pages: list[dict]) -> list:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert merge_pages([{'items': [1]}, {'items': [2, 3]}]) == [1, 2, 3]\n"
            "    assert merge_pages([]) == []\n"
            "    assert merge_pages([{'items': []}]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def merge_pages(pages: list[dict]) -> list:\n"
            "    return [item for page in pages for item in page['items']]\n"
        ),
    },
    {
        "slug": "10_circuit_breaker",
        "track": "apis", "difficulty": "hard",
        "title": "Circuit Breaker",
        "tags": ["api", "state"],
        "description": "A CircuitBreaker starts 'closed'. Record success()/failure(). After `threshold` failures it 'opens'; success() after cooldown resets to 'closed'. Return the current state string.",
        "examples": "cb.state() -> 'closed' / 'open' / 'half_open'",
        "hint": "Track consecutive failures and a state; use time.monotonic() for cooldown.",
        "syntax_hint": "if self.failures >= threshold: self.state = 'open'; self.opened_at = time.monotonic()",
        "signature": (
            "class CircuitBreaker:\n"
            "    pass"
        ),
        "tests": (
            "def run_tests() -> None:\n"
            "    cb = CircuitBreaker(threshold=2, cooldown=1.0)\n"
            "    assert cb.state() == 'closed'\n"
            "    cb.failure(); cb.failure()\n"
            "    assert cb.state() == 'open'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import time\n\n"
            "class CircuitBreaker:\n"
            "    def __init__(self, threshold: int, cooldown: float):\n"
            "        self.threshold = threshold\n"
            "        self.cooldown = cooldown\n"
            "        self.failures = 0\n"
            "        self._state = 'closed'\n"
            "        self.opened_at = 0.0\n"
            "\n"
            "    def state(self) -> str:\n"
            "        if self._state == 'open':\n"
            "            if time.monotonic() - self.opened_at >= self.cooldown:\n"
            "                self._state = 'half_open'\n"
            "        return self._state\n"
            "\n"
            "    def success(self) -> None:\n"
            "        self.failures = 0\n"
            "        self._state = 'closed'\n"
            "\n"
            "    def failure(self) -> None:\n"
            "        self.failures += 1\n"
            "        if self.failures >= self.threshold:\n"
            "            self._state = 'open'\n"
            "            self.opened_at = time.monotonic()\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_http_basics",
        "track": "apis", "difficulty": "easy",
        "title": "HTTP Status & JSON",
        "tags": ["http", "json"],
        "exercise": "content/problems/apis/easy/04_status_class.py",
        "body": (
            "# HTTP & JSON\n\n"
            "Status codes are grouped by their leading digit:\n\n"
            "- 2xx success, 3xx redirect, 4xx client error, 5xx server error.\n\n"
            "API responses are usually JSON. Decode with `json.loads`:\n\n"
            "```python\nimport json\ndata = json.loads(response_text)\n```\n\n"
            "Build query strings with `urllib.parse.urlencode` rather than hand-joining."
        ),
    },
]
