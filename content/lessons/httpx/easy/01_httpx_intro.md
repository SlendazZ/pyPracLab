---
title: HTTPX Basics
track: httpx
difficulty: easy
tags: httpx
exercise: content/problems/httpx/easy/01_build_request.py
---

# HTTPX Basics

## Overview

HTTPX is a modern HTTP client for Python. If you have used `requests`, HTTPX will feel familiar — but it also supports **async** (`await client.get(...)`) and ships with testing tools that do not require a live network.

Think of HTTPX as "requests, plus async and built-in mocking." You still send a method and URL; you still get back a response with status, headers, and body. The API is intentionally similar so migration is easy.

Real-world uses:

- Calling REST APIs from scripts and microservices
- Async services that fan out to many endpoints at once
- Testing FastAPI/Starlette apps with `httpx.ASGITransport`
- Unit tests that mock HTTP without hitting the internet
- HTTP/2 connections to modern APIs (optional extra)

Install with `pip install httpx`. For HTTP/2 support, add the optional `httpx[http2]` extra.

## Your first GET request

The one-liner pattern mirrors `requests` exactly:

```python
import httpx

response = httpx.get('https://httpbin.org/get', timeout=10.0)
response.raise_for_status()   # raise if 4xx or 5xx
data = response.json()
print(data['url'])            # echo of the URL you requested
```

Step by step:
1. `httpx.get(...)` sends an HTTP GET and waits for the response.
2. `raise_for_status()` turns HTTP errors into exceptions you can catch.
3. `.json()` parses the body as JSON (raises if the body is not JSON).

**Always set `timeout=`** in production. Without it, a hung server blocks your worker forever.

## Sync client: GET and POST

For multiple calls to the same host, use a `Client` so TCP connections are reused (faster, fewer sockets):

```python
with httpx.Client(timeout=10.0) as client:
    r = client.get('https://api.example.com/users')
    r.raise_for_status()
    users = r.json()

    created = client.post(
        'https://api.example.com/users',
        json={'name': 'Ada', 'role': 'admin'},
        headers={'Authorization': 'Bearer TOKEN'},
    )
    created.raise_for_status()
    print(created.json())
```

Request body helpers:

| Parameter | Sends as                         | Content-Type                    |
|-----------|----------------------------------|---------------------------------|
| `json=`   | JSON-encoded dict/list           | `application/json` (automatic)  |
| `data=`   | Form fields                      | `application/x-www-form-urlencoded` |
| `content=`| Raw bytes                        | You set headers manually        |
| `files=`  | Multipart upload                 | `multipart/form-data`           |

## base_url on Client

When every call shares a host, set `base_url` once:

```python
with httpx.Client(base_url='https://api.example.com', timeout=10.0) as client:
    users = client.get('/users').json()       # → https://api.example.com/users
    user = client.get('/users/42').json()     # → https://api.example.com/users/42
```

Relative paths join cleanly — no string concatenation bugs.

## Building requests without sending

Construct a `Request` object and inspect it before any network I/O. Ideal for unit tests that verify URL construction:

```python
import httpx

req = httpx.Request(
    'GET',
    'https://api.example.com/search',
    params={'q': 'python', 'page': 2},
)
assert req.method == 'GET'
assert 'q=python' in str(req.url)
assert 'page=2' in str(req.url)
```

HTTPX handles URL encoding — spaces become `%20`, `&` and `=` in values are escaped safely.

**Worked example:** build a search URL helper:

```python
def build_search_request(base_url: str, query: str, page: int = 1) -> httpx.Request:
    return httpx.Request('GET', base_url, params={'q': query, 'page': page})

req = build_search_request('https://shop.example.com/api/search', 'blue socks', page=3)
url = str(req.url)
# https://shop.example.com/api/search?q=blue+socks&page=3
```

**Worked example:** POST with JSON headers (no network):

```python
def build_create_user_request(url: str, payload: dict, token: str) -> httpx.Request:
    return httpx.Request(
        'POST',
        url,
        json=payload,
        headers={'Authorization': f'Bearer {token}'},
    )

req = build_create_user_request(
    'https://api.example.com/users',
    {'name': 'Ada'},
    'secret-token',
)
assert req.method == 'POST'
assert req.headers['Authorization'] == 'Bearer secret-token'
```

## Real-world scenario: paginated API client

```python
def fetch_all_pages(client: httpx.Client, path: str) -> list[dict]:
    results = []
    page = 1
    while True:
        r = client.get(path, params={'page': page, 'limit': 100})
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        results.extend(batch)
        page += 1
    return results
```

Build each page URL with `params=` — never hand-concatenate `?page=` strings.

## Async client

When you need to call many APIs concurrently, async saves wall-clock time:

```python
import asyncio
import httpx

async def fetch_all(urls: list[str]) -> list[dict]:
    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for r in responses:
            r.raise_for_status()
        return [r.json() for r in responses]

results = asyncio.run(fetch_all([
    'https://api.example.com/users/1',
    'https://api.example.com/users/2',
    'https://api.example.com/users/3',
]))
```

Rules for async:
- Use `AsyncClient` inside `async def` functions.
- Do **not** call blocking `httpx.get()` inside FastAPI `async def` routes — that blocks the event loop.
- Either use `async def` + `AsyncClient`, or use sync `def` routes + sync `Client`.

## MockTransport for tests

Replace the network with a handler function that returns canned responses. No internet, no flaky CI:

```python
import httpx

def handler(request: httpx.Request) -> httpx.Response:
    if request.url.path == '/health':
        return httpx.Response(200, json={'status': 'ok'})
    if request.url.path == '/users':
        return httpx.Response(200, json=[{'id': 1, 'name': 'Ada'}])
    return httpx.Response(404, json={'error': 'not found'})

transport = httpx.MockTransport(handler)
with httpx.Client(transport=transport, base_url='https://fake.test') as client:
    assert client.get('/health').json() == {'status': 'ok'}
    assert client.get('/users').json()[0]['name'] == 'Ada'
    assert client.get('/nope').status_code == 404
```

**Worked example:** test a client wrapper without network:

```python
def get_user_name(client: httpx.Client, user_id: int) -> str:
    r = client.get(f'/users/{user_id}')
    r.raise_for_status()
    return r.json()['name']

def mock_handler(request: httpx.Request) -> httpx.Response:
    user_id = request.url.path.split('/')[-1]
    return httpx.Response(200, json={'name': f'User {user_id}'})

with httpx.Client(transport=httpx.MockTransport(mock_handler)) as client:
    assert get_user_name(client, 42) == 'User 42'
```

## ASGITransport: test FastAPI apps

HTTPX can call a FastAPI app directly — no Uvicorn, no open port:

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get('/hello')
def hello():
    return {'message': 'hi'}

transport = httpx.ASGITransport(app=app)
with httpx.Client(transport=transport, base_url='http://test') as client:
    r = client.get('/hello')
    assert r.status_code == 200
    assert r.json() == {'message': 'hi'}
```

This is how `fastapi.testclient.TestClient` works under the hood.

## Sessions, headers, and cookies

```python
with httpx.Client() as client:
    client.headers['User-Agent'] = 'myapp/1.0'
    client.headers['Accept'] = 'application/json'
    r1 = client.get('https://api.example.com/me')
    r2 = client.get('https://api.example.com/settings')
    # both requests share default headers and connection pool
```

Per-request headers merge with client defaults. Cookies persist on the client the same way as `requests.Session`.

## Inspecting responses

```python
r = httpx.get('https://httpbin.org/status/404', timeout=10.0)
r.status_code          # 404
r.headers['content-type']
r.text                 # body as str
r.content              # body as bytes
r.json()               # parse JSON (raises if not JSON)
r.raise_for_status()   # raises httpx.HTTPStatusError on 4xx/5xx
r.elapsed.total_seconds()  # how long the request took
```

Always check status before calling `.json()`. Error pages are often HTML, not JSON — calling `.json()` on a 500 HTML page raises `JSONDecodeError`.

## Error handling pattern

```python
try:
    r = httpx.get(url, timeout=10.0)
    r.raise_for_status()
    data = r.json()
except httpx.TimeoutException:
    print('server too slow')
except httpx.HTTPStatusError as e:
    print(f'HTTP {e.response.status_code}: {e.response.text[:200]}')
except httpx.RequestError as e:
    print(f'network problem: {e}')
```

## HTTPX vs requests

| Feature              | requests | httpx |
|----------------------|----------|-------|
| Sync API             | yes      | yes   |
| Async API            | no       | yes   |
| MockTransport        | no       | yes   |
| ASGI app testing     | no       | yes   |
| HTTP/2 (optional)    | no       | yes   |

For simple sync scripts, either library works. Choose HTTPX when you need async, built-in mocking, or tight integration with FastAPI tests.

## Common pitfalls

- No timeout → hung workers in production
- Calling `.json()` on a 500 HTML error page
- Using sync `httpx.get()` inside `async def` FastAPI routes
- Creating a new `Client` per request (loses connection pooling)
- Putting API keys in query strings (they end up in logs and browser history)
- Retrying POST requests blindly (can duplicate side effects)
- Forgetting `raise_for_status()` and treating 404/500 responses as success

## Practice

Build an httpx Request and inspect its method and URL.

## Summary

HTTPX = requests-like ergonomics + async + MockTransport for tests. Build `Request` objects to verify URL logic; use `Client`/`AsyncClient` for real calls; mock the transport to keep tests fast and offline.
