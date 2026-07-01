"""Servers problem specs (routing, middleware, request/response models)."""

PROBLEMS = [
    {
        "slug": "01_route_matcher",
        "track": "servers", "difficulty": "easy",
        "title": "Route Matcher",
        "tags": ["routing"],
        "description": "Given a dict mapping path -> handler name and a request path, return the handler name, or 'not_found'.",
        "examples": 'match({"/": "home"}, "/health") -> "not_found"',
        "hint": "dict.get with a default.",
        "syntax_hint": "routes.get(path, 'not_found')",
        "signature": "def match(routes: dict[str, str], path: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert match({"/": "home", "/health": "health"}, "/health") == "health"\n'
            '    assert match({"/": "home"}, "/missing") == "not_found"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def match(routes: dict[str, str], path: str) -> str:\n"
            "    return routes.get(path, 'not_found')\n"
        ),
    },
    {
        "slug": "02_middleware_chain",
        "track": "servers", "difficulty": "medium",
        "title": "Middleware Chain",
        "tags": ["pipeline"],
        "description": "Each middleware takes (req, next) and returns a response. Compose a list of middlewares around a final handler into one callable.",
        "examples": "compose(middlewares, final)(req) -> response",
        "hint": "Build the chain from the inside out, wrapping each middleware around the next.",
        "syntax_hint": "for mw in reversed(middlewares): handler = wrap(mw, handler)",
        "signature": "def compose(middlewares: list, final):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    log = []\n"
            "    def mw_a(req, nxt):\n"
            "        log.append('a-in'); r = nxt(req); log.append('a-out'); return r\n"
            "    def mw_b(req, nxt):\n"
            "        log.append('b-in'); r = nxt(req); log.append('b-out'); return r\n"
            "    def final(req):\n"
            "        log.append('final'); return {'status': 200}\n"
            "    handler = compose([mw_a, mw_b], final)\n"
            "    assert handler({'path': '/'}) == {'status': 200}\n"
            "    assert log == ['a-in', 'b-in', 'final', 'b-out', 'a-out']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def compose(middlewares: list, final):\n"
            "    handler = final\n"
            "    for mw in reversed(middlewares):\n"
            "        def make(mw=mw, h=handler):\n"
            "            def wrapped(req):\n"
            "                return mw(req, h)\n"
            "            return wrapped\n"
            "        handler = make()\n"
            "    return handler\n"
        ),
    },
    {
        "slug": "03_simple_router",
        "track": "servers", "difficulty": "easy",
        "title": "Method + Path Router",
        "tags": ["routing"],
        "description": "Return the handler for a (method, path) tuple from a routes dict, or 'not_found'.",
        "examples": 'route({("GET","/"): "home"}, ("GET","/")) -> "home"',
        "hint": "Use the tuple as a dict key.",
        "syntax_hint": "routes.get((method, path), 'not_found')",
        "signature": "def route(routes: dict, method: str, path: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    r = {("GET", "/"): "home", ("POST", "/items"): "create"}\n'
            '    assert route(r, "GET", "/") == "home"\n'
            '    assert route(r, "POST", "/items") == "create"\n'
            '    assert route(r, "DELETE", "/x") == "not_found"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def route(routes: dict, method: str, path: str) -> str:\n"
            "    return routes.get((method, path), 'not_found')\n"
        ),
    },
    {
        "slug": "04_parse_query_string",
        "track": "servers", "difficulty": "easy",
        "title": "Parse Query String",
        "tags": ["url"],
        "description": "Parse a query string 'a=1&b=2' into a dict. Return {} for an empty string.",
        "examples": 'parse_qs("a=1&b=2") -> {"a":"1","b":"2"}',
        "hint": "urllib.parse.parse_qs returns lists; or split on '&' and '='.",
        "syntax_hint": "from urllib.parse import parse_qs; {k: v[0] for k, v in parse_qs(q).items()}",
        "signature": "def parse_qs(q: str) -> dict[str, str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert parse_qs("a=1&b=2") == {"a": "1", "b": "2"}\n'
            '    assert parse_qs("") == {}\n'
            '    assert parse_qs("single=5") == {"single": "5"}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import urllib.parse\n\n"
            "def parse_qs(q: str) -> dict[str, str]:\n"
            "    return {k: v[0] for k, v in urllib.parse.parse_qs(q).items()}\n"
        ),
    },
    {
        "slug": "05_split_path_segments",
        "track": "servers", "difficulty": "easy",
        "title": "Split Path Segments",
        "tags": ["string"],
        "description": "Return the non-empty segments of a URL path, splitting on '/'.",
        "examples": 'segments("/a/b//c/") -> ["a","b","c"]',
        "hint": "Split on '/' and drop empty strings.",
        "syntax_hint": "[s for s in path.split('/') if s]",
        "signature": "def segments(path: str) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert segments("/a/b//c/") == ["a", "b", "c"]\n'
            '    assert segments("/") == []\n'
            '    assert segments("/items/42") == ["items", "42"]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def segments(path: str) -> list[str]:\n"
            "    return [s for s in path.split('/') if s]\n"
        ),
    },
    {
        "slug": "06_pattern_router",
        "track": "servers", "difficulty": "medium",
        "title": "Pattern Router",
        "tags": ["routing", "regex"],
        "description": "Given routes as a list of (pattern, handler) where pattern may contain '<name>', return (handler, params_dict) for the first matching path, or (None, {}).",
        "examples": 'route([("/users/<id>", "show")], "/users/42") -> ("show", {"id": "42"})',
        "hint": "Convert '<name>' to a named regex group and match.",
        "syntax_hint": "re.sub(r'<(\\w+)>', r'(?P<\\1>[^/]+)', pattern)",
        "signature": "def route(routes: list[tuple[str, str]], path: str) -> tuple:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    routes = [('/users/<id>', 'show'), ('/', 'index')]\n"
            '    assert route(routes, "/users/42") == ("show", {"id": "42"})\n'
            '    assert route(routes, "/") == ("index", {})\n'
            '    assert route(routes, "/missing") == (None, {})\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import re\n\n"
            "def route(routes: list[tuple[str, str]], path: str) -> tuple:\n"
            "    for pattern, handler in routes:\n"
            "        regex = '^' + re.sub(r'<(\\w+)>', r'(?P<\\1>[^/]+)', pattern) + '$'\n"
            "        m = re.match(regex, path)\n"
            "        if m:\n"
            "            return handler, m.groupdict()\n"
            "    return None, {}\n"
        ),
    },
    {
        "slug": "07_status_line",
        "track": "servers", "difficulty": "easy",
        "title": "Build Status Line",
        "tags": ["http"],
        "description": "Return an HTTP status line like 'HTTP/1.1 200 OK' given a status code and reason.",
        "examples": 'status_line(200, "OK") -> "HTTP/1.1 200 OK"',
        "hint": "Simple f-string formatting.",
        "syntax_hint": 'f"HTTP/1.1 {code} {reason}"',
        "signature": "def status_line(code: int, reason: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert status_line(200, "OK") == "HTTP/1.1 200 OK"\n'
            '    assert status_line(404, "Not Found") == "HTTP/1.1 404 Not Found"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def status_line(code: int, reason: str) -> str:\n"
            "    return f\"HTTP/1.1 {code} {reason}\"\n"
        ),
    },
    {
        "slug": "08_keep_alive_headers",
        "track": "servers", "difficulty": "easy",
        "title": "Header Parser",
        "tags": ["http", "string"],
        "description": "Parse raw header lines 'Key: Value' into a dict with lowercased keys.",
        "examples": 'parse_headers("Content-Type: json\\nX-Trace: 1") -> {"content-type":"json","x-trace":"1"}',
        "hint": "Split each line on the first ': '.",
        "syntax_hint": "k, v = line.split(': ', 1); d[k.lower()] = v",
        "signature": "def parse_headers(text: str) -> dict[str, str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert parse_headers("Content-Type: json\\nX-Trace: 1") == {"content-type": "json", "x-trace": "1"}\n'
            '    assert parse_headers("") == {}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def parse_headers(text: str) -> dict[str, str]:\n"
            "    out = {}\n"
            "    for line in text.splitlines():\n"
            "        if ': ' in line:\n"
            "            k, v = line.split(': ', 1)\n"
            "            out[k.lower()] = v\n"
            "    return out\n"
        ),
    },
    {
        "slug": "09_static_file_map",
        "track": "servers", "difficulty": "easy",
        "title": "Static File Map",
        "tags": ["dict", "mime"],
        "description": "Given a list of filenames, return a dict mapping each name to a mime guessed from its extension ('.html'->'text/html', '.css'->'text/css', '.js'->'application/javascript', else 'application/octet-stream').",
        "examples": 'mimes(["a.html","b.css"]) -> {"a.html":"text/html","b.css":"text/css"}',
        "hint": "A small dict of extension -> mime does the job.",
        "syntax_hint": "ext = name.rsplit('.', 1)[-1] if '.' in name else ''",
        "signature": "def mimes(names: list[str]) -> dict[str, str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert mimes(["a.html", "b.css"]) == {"a.html": "text/html", "b.css": "text/css"}\n'
            '    assert mimes(["app.js"]) == {"app.js": "application/javascript"}\n'
            '    assert mimes(["noext"]) == {"noext": "application/octet-stream"}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def mimes(names: list[str]) -> dict[str, str]:\n"
            "    table = {'html': 'text/html', 'css': 'text/css', 'js': 'application/javascript'}\n"
            "    out = {}\n"
            "    for name in names:\n"
            "        ext = name.rsplit('.', 1)[-1].lower() if '.' in name else ''\n"
            "        out[name] = table.get(ext, 'application/octet-stream')\n"
            "    return out\n"
        ),
    },
    {
        "slug": "10_request_log_line",
        "track": "servers", "difficulty": "easy",
        "title": "Request Log Line",
        "tags": ["string"],
        "description": "Return a common-log-format style line: 'METHOD PATH STATUS SIZE'.",
        "examples": 'log_line("GET", "/a", 200, 12) -> "GET /a 200 12"',
        "hint": "f-string joins the four parts.",
        "syntax_hint": 'f"{method} {path} {status} {size}"',
        "signature": "def log_line(method: str, path: str, status: int, size: int) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert log_line("GET", "/a", 200, 12) == "GET /a 200 12"\n'
            '    assert log_line("POST", "/x", 500, 0) == "POST /x 500 0"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def log_line(method: str, path: str, status: int, size: int) -> str:\n"
            "    return f\"{method} {path} {status} {size}\"\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_routing",
        "track": "servers", "difficulty": "easy",
        "title": "Request Routing",
        "tags": ["routing"],
        "exercise": "content/problems/servers/easy/01_route_matcher.py",
        "body": (
            "# Routing\n\n"
            "Routing maps a request to a handler. The simplest form is a dict lookup:\n\n"
            "```python\nroutes = {'/': home, '/health': health}\nhandler = routes.get(path, not_found)\n```\n\n"
            "When you need parameters, swap the literal segment for a placeholder and "
            "match with a regex (`/users/<id>` -> `(?P<id>[^/]+)`)."
        ),
    },
]
