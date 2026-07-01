---
title: Request Routing
track: servers
difficulty: easy
tags: routing
exercise: content/problems/servers/easy/01_route_matcher.py
---

# Request Routing

## Overview

Routing maps an incoming request (method + path) to the code that handles it. Every web framework — from a 50-line stdlib server to FastAPI — has a router at its core.

When a browser requests `GET /users/42`, the server must answer two questions: which function runs, and what is `42`? Routing is that decision step — classify the request, extract parameters, call the handler, return a response.

If you have written `if path == '/health':` in a script, you already understand routing at a basic level. Production routers add patterns, method checks, and clean 404/405 responses.

## Static routes

The simplest router is a dictionary lookup keyed by method and path:

```python
def home(request):
    return {'status': 200, 'body': 'welcome'}

def health(request):
    return {'status': 200, 'body': 'ok'}

def not_found(request):
    return {'status': 404, 'body': 'not found'}

routes = {
    ('GET', '/'): home,
    ('GET', '/health'): health,
}

def dispatch(method: str, path: str, request: dict) -> dict:
    handler = routes.get((method, path), not_found)
    return handler(request)
```

Try it in the REPL:

```python
dispatch('GET', '/health', {})   # {'status': 200, 'body': 'ok'}
dispatch('GET', '/missing', {})  # {'status': 404, ...}
```

This works for fixed paths. Real APIs need paths with variable segments.

## Path parameters

When a segment varies (`/users/42`), match with a pattern and capture groups:

```python
import re

USER_PATTERN = re.compile(r'^/users/(?P<id>\d+)$')

def match_user(path: str) -> dict | None:
    m = USER_PATTERN.match(path)
    if m:
        return {'id': int(m.group('id'))}
    return None

match_user('/users/42')   # {'id': 42}
match_user('/users/abc')  # None
```

Frameworks expose the same idea as `/users/{id}` or `/users/<id>` — you write a template; the framework compiles it to a regex or trie.

Convert captured strings to the types your handler expects:

```python
def get_user(path: str) -> dict | None:
    params = match_user(path)
    if params is None:
        return None
    user_id = params['id']
    return {'id': user_id, 'name': f'User {user_id}'}
```

## Worked example: template matcher

Convert a path template into a regex and extract named groups:

```python
import re

def compile_template(template: str) -> re.Pattern:
    parts = []
    for segment in template.strip('/').split('/'):
        if segment.startswith('{') and segment.endswith('}'):
            name = segment[1:-1]
            parts.append(f'(?P<{name}>[^/]+)')
        else:
            parts.append(re.escape(segment))
    pattern = '^/' + '/'.join(parts) + '$'
    return re.compile(pattern)

route = compile_template('/users/{id}/posts/{slug}')
m = route.match('/users/42/posts/hello-world')
m.groupdict()  # {'id': '42', 'slug': 'hello-world'}
```

Step by step:
1. Split the template on `/`.
2. `{id}` becomes a named capture group `(?P<id>[^/]+)`.
3. Literal segments are escaped so `.` does not mean any character.
4. `^` and `$` anchor the match to the full path.

Build a small router that tries templates in order:

```python
TEMPLATES = [
    ('/users/{id}', get_user_handler),
    ('/health', health_handler),
]
COMPILED = [(compile_template(t), fn) for t, fn in TEMPLATES]

def route_request(method: str, path: str) -> dict:
    for pattern, handler in COMPILED:
        m = pattern.match(path)
        if m:
            return handler(method, m.groupdict())
    return {'status': 404, 'body': 'not found'}
```

Register specific paths before wildcards so `/users/me` is not captured as `{id}`.

## Method-aware routing

The same path can mean different things for different HTTP methods:

```python
routes = {
    ('GET', '/items'): list_items,
    ('POST', '/items'): create_item,
}

def dispatch(method: str, path: str, request: dict) -> dict:
    handler = routes.get((method, path))
    if handler is None:
        if any(k[1] == path for k in routes):
            return {'status': 405, 'body': 'method not allowed'}
        return {'status': 404, 'body': 'not found'}
    return handler(request)
```

```
GET  /items  → list
POST /items  → create
```

Always key routes by `(method, path)` tuple or equivalent. Return 405 Method Not Allowed when the path exists but the verb does not.

Worked example: distinguish 404 vs 405:

```python
routes = {('GET', '/items'): list_items}

dispatch('DELETE', '/items', {})  # 405 — path exists, method wrong
dispatch('GET', '/orders', {})    # 404 — path unknown
```

## Middleware order

Request flows through layers before your handler runs:

```
socket → parse request → middleware chain → router → handler → response
```

Auth and logging middleware run before the router; error handlers wrap the outside so exceptions become proper HTTP responses.

The router sits *after* parsing (you need method and path) but *before* business logic (the handler should receive extracted params).

## Worked example: end-to-end mini server flow

Tie routing pieces together without a framework:

```python
def handle_request(method: str, path: str) -> dict:
    static = routes.get((method, path))
    if static:
        return static({})
    params = match_user(path)
    if params and method == 'GET':
        return {'status': 200, 'body': f'user {params["id"]}'}
    if params:
        return {'status': 405, 'body': 'method not allowed'}
    return {'status': 404, 'body': 'not found'}
```

## Common pitfalls

- Trailing slash mismatches (`/users` vs `/users/`) — pick one convention
- Greedy patterns that swallow too much of the path — use `[^/]+` per segment
- Forgetting to return 405 Method Not Allowed for wrong verb
- Matching routes in arbitrary order — register specific paths before wildcards
- Leaving captured params as strings when you need `int` or `UUID`
- Case-sensitive paths on Linux — `/Users` and `/users` are different

## Practice

Implement a matcher that extracts named groups from a path template.

## Summary

Routing = classify request → call handler. Start with dict lookup; add regex or trie when paths have parameters. Key by `(method, path)`, extract params with named groups, and distinguish 404 (unknown path) from 405 (wrong method).
