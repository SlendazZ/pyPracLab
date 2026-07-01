"""requests problem specs."""

PROBLEMS = [
    {
        "slug": "01_build_request",
        "track": "requests", "difficulty": "easy",
        "title": "Build a Prepared Request",
        "tags": ["requests", "url"],
        "description": "Using requests, build and return a PreparedRequest for the given method, url, and query params (no network call).",
        "examples": "build_request('GET', 'https://x.test/api', {'q': 'py'}) -> req with q=py in url",
        "hint": "requests.Request(method, url, params=...).prepare().",
        "syntax_hint": "from requests import Request; Request('GET', url, params=p).prepare()",
        "signature": "def build_request(method: str, url: str, params: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    req = build_request('GET', 'https://x.test/api', {'q': 'py', 'page': '1'})\n"
            "    assert req.method == 'GET'\n"
            "    assert 'q=py' in req.url and 'page=1' in req.url\n"
            "    assert req.url.startswith('https://x.test/api')\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from requests import Request\n\n"
            "def build_request(method: str, url: str, params: dict):\n"
            "    return Request(method, url, params=params).prepare()\n"
        ),
    },
    {
        "slug": "02_set_headers",
        "track": "requests", "difficulty": "easy",
        "title": "Set Request Headers",
        "tags": ["requests", "headers"],
        "description": "Build a PreparedRequest with the given headers dict and verify via .headers.",
        "examples": "headers on req include 'Authorization'",
        "hint": "Request(method, url, headers=...).prepare().",
        "syntax_hint": "Request('GET', url, headers={'Authorization': 'Bearer x'}).prepare()",
        "signature": "def build_with_headers(method: str, url: str, headers: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    req = build_with_headers('GET', 'https://x.test/api', {'Authorization': 'Bearer x'})\n"
            "    assert req.headers['Authorization'] == 'Bearer x'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from requests import Request\n\n"
            "def build_with_headers(method: str, url: str, headers: dict):\n"
            "    return Request(method, url, headers=headers).prepare()\n"
        ),
    },
    {
        "slug": "03_session_adapter",
        "track": "requests", "difficulty": "medium",
        "title": "Session Base Headers",
        "tags": ["requests", "session"],
        "description": "Return a requests.Session whose default headers include 'User-Agent': 'pyprac/1.0'. (No network call.)",
        "examples": "session.headers['User-Agent'] == 'pyprac/1.0'",
        "hint": "session.headers is a dict-like; assign into it.",
        "syntax_hint": "s = requests.Session(); s.headers['User-Agent'] = 'pyprac/1.0'",
        "signature": "def make_session():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import requests\n"
            "    s = make_session()\n"
            "    assert isinstance(s, requests.Session)\n"
            "    assert s.headers['User-Agent'] == 'pyprac/1.0'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import requests\n\n"
            "def make_session():\n"
            "    s = requests.Session()\n"
            "    s.headers['User-Agent'] = 'pyprac/1.0'\n"
            "    return s\n"
        ),
    },
    {
        "slug": "04_dedupe_query",
        "track": "requests", "difficulty": "easy",
        "title": "Dedupe Query Params",
        "tags": ["requests", "url"],
        "description": "Given a dict of params (possibly with None values), return a PreparedRequest whose url contains only the non-None params.",
        "examples": "url excludes None params",
        "hint": "Filter None before passing to Request.",
        "syntax_hint": "{k: v for k, v in params.items() if v is not None}",
        "signature": "def build_clean(url: str, params: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    req = build_clean('https://x.test/api', {'q': 'py', 'n': None})\n"
            "    assert 'q=py' in req.url\n"
            "    assert 'n=' not in req.url\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from requests import Request\n\n"
            "def build_clean(url: str, params: dict):\n"
            "    clean = {k: v for k, v in params.items() if v is not None}\n"
            "    return Request('GET', url, params=clean).prepare()\n"
        ),
    },
    {
        "slug": "05_retry_session",
        "track": "requests", "difficulty": "hard",
        "title": "Retry Session",
        "tags": ["requests", "retry"],
        "description": "Return a requests.Session mounted with an HTTPAdapter that retries up to 3 times on 500/502/503/504 with backoff 0.3. (No network call.)",
        "examples": "adapter has max_retries=3",
        "hint": "from requests.adapters import HTTPAdapter; from urllib3.util.retry import Retry.",
        "syntax_hint": "Retry(total=3, backoff_factor=0.3, status_forcelist=[500,502,503,504])",
        "signature": "def make_retry_session():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import requests\n"
            "    from requests.adapters import HTTPAdapter\n"
            "    s = make_retry_session()\n"
            "    assert isinstance(s, requests.Session)\n"
            "    adapter = s.get_adapter('https://x.test')\n"
            "    assert isinstance(adapter, HTTPAdapter)\n"
            "    assert adapter.max_retries.total == 3\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import requests\nfrom requests.adapters import HTTPAdapter\n"
            "try:\n    from urllib3.util.retry import Retry\nexcept ImportError:\n    from requests.packages.urllib3.util.retry import Retry\n\n"
            "def make_retry_session():\n"
            "    s = requests.Session()\n"
            "    retry = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])\n"
            "    adapter = HTTPAdapter(max_retries=retry)\n"
            "    s.mount('http://', adapter)\n"
            "    s.mount('https://', adapter)\n"
            "    return s\n"
        ),
    },
    {
        "slug": "06_cookie_jar",
        "track": "requests", "difficulty": "medium",
        "title": "Preload Cookies",
        "tags": ["requests", "cookies"],
        "description": "Return a requests.Session with cookies from the given dict set on it (no network call).",
        "examples": "session.cookies.get('token') == 'abc'",
        "hint": "session.cookies.update(dict) sets cookies.",
        "syntax_hint": "s.cookies.update({'token': 'abc'})",
        "signature": "def make_session_with_cookies(cookies: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    s = make_session_with_cookies({'token': 'abc', 'theme': 'dark'})\n"
            "    assert s.cookies.get('token') == 'abc'\n"
            "    assert s.cookies.get('theme') == 'dark'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import requests\n\n"
            "def make_session_with_cookies(cookies: dict):\n"
            "    s = requests.Session()\n"
            "    s.cookies.update(cookies)\n"
            "    return s\n"
        ),
    },
    {
        "slug": "07_timeout_value",
        "track": "requests", "difficulty": "easy",
        "title": "Build a Timeout Tuple",
        "tags": ["requests"],
        "description": "Given connect and read seconds, return the requests-style timeout tuple (connect, read).",
        "examples": "timeout_tuple(2, 5) -> (2, 5)",
        "hint": "requests accepts a (connect, read) tuple for timeout.",
        "syntax_hint": "return (connect, read)",
        "signature": "def timeout_tuple(connect: float, read: float) -> tuple:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert timeout_tuple(2, 5) == (2, 5)\n"
            "    assert timeout_tuple(0.5, 1.5) == (0.5, 1.5)\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def timeout_tuple(connect: float, read: float) -> tuple:\n"
            "    return (connect, read)\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_requests_intro",
        "track": "requests", "difficulty": "easy",
        "title": "requests: Requests Without Network",
        "tags": ["requests"],
        "exercise": "content/problems/requests/easy/01_build_request.py",
        "body": (
            "# requests\n\n"
            "The `requests` library also lets you build requests *without* sending them, "
            "which is great for testing URL/header construction:\n\n"
            "```python\nfrom requests import Request\nreq = Request('GET', url, params={'q': 'py'}).prepare()\n"
            "assert 'q=py' in req.url\n```\n\n"
            "Use `Session()` to share headers, cookies, and retry adapters across calls."
        ),
    },
]
