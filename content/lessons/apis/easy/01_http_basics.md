---
title: HTTP Status Codes and JSON
track: apis
difficulty: easy
tags: http, json
exercise: content/problems/apis/easy/04_status_class.py
---

# HTTP Status Codes and JSON

## Overview

HTTP is the protocol behind web APIs. Clients send requests (method, URL, headers, body); servers respond with status, headers, and body. Most REST APIs return JSON in the body.

You do not need to memorize every header on day one. Focus on three ideas: what you are asking for (method + URL), whether it worked (status code), and the payload (usually JSON text in the body).

Think of an API call like ordering at a restaurant: you state what you want (GET /menu), the kitchen replies with a code (200 = here you go, 404 = that item is not on the menu), and the plate is the response body.

## Request anatomy

A raw HTTP request has a request line, headers, and an optional body:

```
GET /users?page=2 HTTP/1.1
Host: api.example.com
Accept: application/json

```

Common methods and their usual meaning:

| Method | Typical use              |
|--------|--------------------------|
| GET    | Read data (no body)      |
| POST   | Create a new resource    |
| PUT    | Replace a resource       |
| PATCH  | Update part of a resource|
| DELETE | Remove a resource        |

The response mirrors this structure: status line, headers, body.

```
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 1, "name": "Ada"}
```

Headers are key-value metadata. `Content-Type: application/json` tells the client how to interpret the body. `Accept: application/json` on the request tells the server what format you prefer back.

## Status code families

The three-digit status code tells you the outcome at a glance:

| Range | Meaning        | Examples              |
|-------|----------------|-----------------------|
| 1xx   | informational  | 100 Continue          |
| 2xx   | success        | 200 OK, 201 Created   |
| 3xx   | redirect       | 301 Moved, 304 Not Modified |
| 4xx   | client error   | 400 Bad Request, 404 Not Found, 401 Unauthorized |
| 5xx   | server error   | 500 Internal Error    |

Classify by the first digit — the status *family*:

```python
def status_class(code: int) -> int:
    return code // 100

status_class(404)  # 4 — client error
status_class(201)  # 2 — success
```

In practice you branch on specific codes or ranges:

```python
def is_success(code: int) -> bool:
    return 200 <= code < 300

def is_client_error(code: int) -> bool:
    return 400 <= code < 500

def describe_status(code: int) -> str:
    if is_success(code):
        return 'ok'
    if code == 404:
        return 'not found'
    if code == 429:
        return 'rate limited — slow down'
    if 500 <= code < 600:
        return 'server error — retry later'
    return f'unexpected status {code}'
```

Memorize a handful you will see daily: 200, 201, 204, 400, 401, 403, 404, 409, 422, 429, 500.

## Worked example: handle a response safely

Never assume the body is JSON or that a 404 is fine:

```python
import json

def parse_api_response(status: int, body: str) -> dict:
    if not (200 <= status < 300):
        raise RuntimeError(f'HTTP {status}: {body[:200]}')
    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValueError('expected JSON body') from exc
```

Step by step:
1. Check the status before parsing — 4xx/5xx responses may return HTML error pages.
2. `json.loads` on the response text converts JSON → Python dict/list.
3. Wrap decode errors so callers know the server returned non-JSON.

Walk through two scenarios:

```python
# Success
data = parse_api_response(200, '{"id": 1, "name": "Ada"}')
print(data['name'])   # Ada

# Failure — raises before json.loads runs
parse_api_response(404, '<html>Not Found</html>')
```

Libraries like `requests` and `httpx` expose `.json()` but you should still check `.status_code` or call `.raise_for_status()` first:

```python
# import httpx
# response = httpx.get('https://api.example.com/users/1')
# response.raise_for_status()
# data = response.json()
```

## JSON in Python

JSON maps directly to Python types you already know:

```python
import json

payload = {'name': 'Ada', 'active': True, 'tags': ['python', 'api']}
body = json.dumps(payload)              # dict → JSON string
data = json.loads('{"id": 42}')       # JSON string → dict
```

Nested structures round-trip cleanly:

```python
user = {
    'id': 42,
    'profile': {'city': 'London', 'skills': ['python', 'http']},
}
text = json.dumps(user, indent=2)
restored = json.loads(text)
assert restored['profile']['skills'][0] == 'python'
```

Sending JSON in a POST body (conceptually):

```python
import json

headers = {'Content-Type': 'application/json'}
body = json.dumps({'email': 'ada@example.com'})
# client.post(url, data=body, headers=headers)
```

`Content-Type: application/json` tells the server how to interpret the body.

## Worked example: build and parse a mock exchange

Practice the full round trip without a network:

```python
import json

def create_user_request(email: str) -> tuple[str, dict, str]:
    method = 'POST'
    headers = {'Content-Type': 'application/json'}
    body = json.dumps({'email': email})
    return method, headers, body

def handle_create_user(status: int, body: str) -> dict:
    if status == 201:
        return json.loads(body)
    if status == 409:
        raise ValueError('email already registered')
    raise RuntimeError(f'unexpected status {status}')

_, _, req_body = create_user_request('ada@example.com')
resp_body = json.dumps({'id': 7, 'email': 'ada@example.com'})
user = handle_create_user(201, resp_body)
print(user['id'])   # 7
```

## Query strings

Query parameters append key-value pairs after `?` in the URL:

```
https://api.example.com/search?q=python&page=2
```

Build them safely — never hand-join user input (spaces, `&`, and `=` need escaping):

```python
from urllib.parse import urlencode

params = {'q': 'python tutorial', 'page': 2}
qs = urlencode(params)
url = f'https://api.example.com/search?{qs}'
# https://api.example.com/search?q=python+tutorial&page=2
```

For multiple values per key, pass a sequence:

```python
urlencode([('tag', 'python'), ('tag', 'api')])
# 'tag=python&tag=api'
```

Parse an existing URL to read parameters back:

```python
from urllib.parse import urlparse, parse_qs

parts = urlparse('https://api.example.com/search?q=python&page=2')
parse_qs(parts.query)   # {'q': ['python'], 'page': ['2']}
```

Note: `parse_qs` values are lists because keys can repeat.

## Common pitfalls

- Treating 404 as success — always check status
- Assuming JSON body on error responses (may be HTML)
- Ignoring rate limits (429) and retry-after headers
- Forgetting to set `Content-Type` when sending JSON
- Comparing float JSON numbers with `==` — rounding surprises
- Logging full response bodies that contain passwords or tokens

## Practice

Write a helper that returns the status class (2, 4, 5, etc.).

## Summary

Know methods, status families, and JSON encode/decode — the foundation for every HTTP client and server exercise in this track. Check status first, parse JSON second, and build URLs with `urlencode`.
