"""httpx problem specs."""

PROBLEMS = [
    {
        "slug": "01_build_request",
        "track": "httpx", "difficulty": "easy",
        "title": "Build an HTTPX Request",
        "tags": ["httpx", "url"],
        "description": "Using httpx, build and return a Request for the given method and url (no network call).",
        "examples": "build_request('GET', 'https://x.test/api') -> Request with method GET",
        "hint": "httpx.Request(method, url) constructs a request object.",
        "syntax_hint": "import httpx; return httpx.Request('GET', url)",
        "signature": "def build_request(method: str, url: str):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import httpx\n"
            "    req = build_request('GET', 'https://x.test/api')\n"
            "    assert isinstance(req, httpx.Request)\n"
            "    assert req.method == 'GET'\n"
            "    assert str(req.url) == 'https://x.test/api'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import httpx\n\n"
            "def build_request(method: str, url: str):\n"
            "    return httpx.Request(method, url)\n"
        ),
    },
    {
        "slug": "02_query_params",
        "track": "httpx", "difficulty": "easy",
        "title": "Query Params on URL",
        "tags": ["httpx", "url"],
        "description": "Build an httpx Request whose URL includes the given query params (no network call).",
        "examples": "build_with_params(url, {'q': 'py'}) -> url contains q=py",
        "hint": "Pass params= to httpx.Request; inspect str(request.url).",
        "syntax_hint": "httpx.Request('GET', url, params={'q': 'py'})",
        "signature": "def build_with_params(url: str, params: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    req = build_with_params('https://x.test/api', {'q': 'py', 'page': '1'})\n"
            "    u = str(req.url)\n"
            "    assert 'q=py' in u and 'page=1' in u\n"
            "    assert u.startswith('https://x.test/api')\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import httpx\n\n"
            "def build_with_params(url: str, params: dict):\n"
            "    return httpx.Request('GET', url, params=params)\n"
        ),
    },
    {
        "slug": "03_custom_headers",
        "track": "httpx", "difficulty": "easy",
        "title": "Custom Request Headers",
        "tags": ["httpx", "headers"],
        "description": "Build an httpx Request with the given headers dict (no network call).",
        "examples": "request.headers['Authorization'] == 'Bearer x'",
        "hint": "Pass headers= to httpx.Request.",
        "syntax_hint": "httpx.Request('GET', url, headers={'Authorization': 'Bearer x'})",
        "signature": "def build_with_headers(url: str, headers: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    req = build_with_headers('https://x.test/api', {'Authorization': 'Bearer x'})\n"
            "    assert req.headers['Authorization'] == 'Bearer x'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import httpx\n\n"
            "def build_with_headers(url: str, headers: dict):\n"
            "    return httpx.Request('GET', url, headers=headers)\n"
        ),
    },
    {
        "slug": "04_post_json",
        "track": "httpx", "difficulty": "medium",
        "title": "POST JSON Body",
        "tags": ["httpx", "json"],
        "description": "Build an httpx Request for POST with a JSON body from the given dict (no network call). Content-Type should be application/json.",
        "examples": "post_json(url, {'name': 'eli'}) has JSON body",
        "hint": "Use json= in httpx.Request for automatic JSON encoding.",
        "syntax_hint": "httpx.Request('POST', url, json={'name': 'eli'})",
        "signature": "def post_json(url: str, payload: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import json\n"
            "    req = post_json('https://x.test/api', {'name': 'eli', 'age': 30})\n"
            "    assert req.method == 'POST'\n"
            "    assert json.loads(req.content) == {'name': 'eli', 'age': 30}\n"
            "    assert 'application/json' in req.headers.get('content-type', '')\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import httpx\n\n"
            "def post_json(url: str, payload: dict):\n"
            "    return httpx.Request('POST', url, json=payload)\n"
        ),
    },
    {
        "slug": "05_basic_auth",
        "track": "httpx", "difficulty": "medium",
        "title": "Basic Auth on Client",
        "tags": ["httpx", "auth"],
        "description": "Return an httpx.Client configured with HTTP basic auth for the given username and password, using MockTransport so no real network call is made.",
        "examples": "client built with auth=('u', 'p')",
        "hint": "httpx.Client(auth=(user, password), transport=MockTransport(handler)).",
        "syntax_hint": "import httpx; httpx.Client(auth=('u', 'p'), transport=httpx.MockTransport(handler))",
        "signature": "def make_auth_client(user: str, password: str):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import httpx\n"
            "    import base64\n"
            "    captured = {}\n"
            "    def handler(request):\n"
            "        captured['auth'] = request.headers.get('authorization')\n"
            "        return httpx.Response(200, json={'ok': True})\n"
            "    client = make_auth_client('u', 'p')\n"
            "    client._transport = httpx.MockTransport(handler)\n"
            "    r = client.get('https://x.test/secure')\n"
            "    assert r.status_code == 200\n"
            "    token = base64.b64encode(b'u:p').decode()\n"
            "    assert captured['auth'] == f'Basic {token}'\n"
            "    client.close()\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import httpx\n\n"
            "def make_auth_client(user: str, password: str):\n"
            "    def handler(request):\n"
            "        return httpx.Response(200, json={'ok': True})\n"
            "    return httpx.Client(\n"
            "        auth=(user, password),\n"
            "        transport=httpx.MockTransport(handler),\n"
            "    )\n"
        ),
    },
    {
        "slug": "06_mock_transport",
        "track": "httpx", "difficulty": "medium",
        "title": "MockTransport Handler",
        "tags": ["httpx", "testing"],
        "description": "Return a function that uses httpx.Client with MockTransport to GET the url and return the JSON body from a fixed {'message': 'ok'} response.",
        "examples": "fetch_json('https://x.test/api') -> {'message': 'ok'}",
        "hint": "Define a handler returning httpx.Response(200, json={...}); use MockTransport(handler).",
        "syntax_hint": "def handler(req): return httpx.Response(200, json={'message': 'ok'})",
        "signature": "def fetch_json(url: str) -> dict:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert fetch_json('https://x.test/api') == {'message': 'ok'}\n"
            "    assert fetch_json('https://other.test/') == {'message': 'ok'}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import httpx\n\n"
            "def fetch_json(url: str) -> dict:\n"
            "    def handler(request):\n"
            "        return httpx.Response(200, json={'message': 'ok'})\n"
            "    with httpx.Client(transport=httpx.MockTransport(handler)) as client:\n"
            "        return client.get(url).json()\n"
        ),
    },
    {
        "slug": "07_timeout_config",
        "track": "httpx", "difficulty": "medium",
        "title": "Timeout Configuration",
        "tags": ["httpx"],
        "description": "Given connect and read seconds, return an httpx.Timeout with those values (set all four phases explicitly).",
        "examples": "make_timeout(2.0, 5.0) -> Timeout with connect=2.0 and read=5.0",
        "hint": "httpx.Timeout requires all four phases or a single default; set connect, read, write, and pool.",
        "syntax_hint": "httpx.Timeout(connect=2.0, read=5.0, write=5.0, pool=5.0)",
        "signature": "def make_timeout(connect: float, read: float):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import httpx\n"
            "    t = make_timeout(2.0, 5.0)\n"
            "    assert isinstance(t, httpx.Timeout)\n"
            "    assert t.connect == 2.0\n"
            "    assert t.read == 5.0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import httpx\n\n"
            "def make_timeout(connect: float, read: float):\n"
            "    return httpx.Timeout(connect=connect, read=read, write=read, pool=connect)\n"
        ),
    },
    {
        "slug": "08_retry_statuses",
        "track": "httpx", "difficulty": "hard",
        "title": "Retry on Status Codes",
        "tags": ["httpx", "retry"],
        "description": "Using httpx.Client with MockTransport, retry a GET up to max_attempts times when the response status is in retry_statuses. Return the final response status code.",
        "examples": "retry_get(client_fn, 503, 200) -> 200 after retries",
        "hint": "Loop up to max_attempts; on retryable status, continue; return last response.",
        "syntax_hint": "for attempt in range(max_attempts): r = client.get(url); if r.status_code not in retry_statuses: return r.status_code",
        "signature": (
            "def retry_get(client, url: str, max_attempts: int, retry_statuses: set[int]) -> int:\n"
            "    pass"
        ),
        "tests": (
            "def run_tests() -> None:\n"
            "    import httpx\n"
            "    calls = {'n': 0}\n"
            "    def handler(request):\n"
            "        calls['n'] += 1\n"
            "        if calls['n'] < 3:\n"
            "            return httpx.Response(503)\n"
            "        return httpx.Response(200)\n"
            "    with httpx.Client(transport=httpx.MockTransport(handler)) as client:\n"
            "        code = retry_get(client, 'https://x.test/api', 5, {503})\n"
            "    assert code == 200\n"
            "    assert calls['n'] == 3\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def retry_get(client, url: str, max_attempts: int, retry_statuses: set[int]) -> int:\n"
            "    last = 0\n"
            "    for _ in range(max_attempts):\n"
            "        response = client.get(url)\n"
            "        last = response.status_code\n"
            "        if last not in retry_statuses:\n"
            "            return last\n"
            "    return last\n"
        ),
    },
]
