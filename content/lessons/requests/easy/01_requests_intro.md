---
title: The requests Library
track: requests
difficulty: easy
tags: requests
exercise: content/problems/requests/easy/01_build_request.py
---

# The requests Library

## Overview

`requests` is the de facto HTTP client for Python. It wraps urllib3 with a simple, readable API — most scripts that call a web API use it. You send a method and URL; you get back a `Response` with status, headers, and body.

Real-world uses:

- Fetching data from public APIs (weather, GitHub, payment providers)
- Posting webhooks or form submissions
- Downloading files and images
- Integration tests against staging servers

Install with `pip install requests`.

## Basic GET

```python
import requests

response = requests.get('https://api.example.com/users', timeout=10)
response.raise_for_status()  # raises on 4xx/5xx
data = response.json()
print(data[0]['name'])
```

**Always set `timeout=`** in production. Without it, a hung server blocks your process indefinitely.

Inspect the response:

```python
response.status_code              # 200
response.headers                  # case-insensitive dict-like
response.headers.get('Content-Type')
response.text                     # str body
response.content                  # bytes body
response.elapsed.total_seconds()  # request duration
response.url                      # final URL (after redirects)
```

## POST with JSON

```python
response = requests.post(
    'https://api.example.com/users',
    json={'name': 'Ada', 'role': 'admin'},
    headers={'Authorization': 'Bearer TOKEN'},
    timeout=10,
)
response.raise_for_status()
new_user = response.json()
```

- `json=` — serializes a dict to JSON and sets `Content-Type: application/json`
- `data=` — form-encoded body (`application/x-www-form-urlencoded`)
- `files=` — multipart uploads

**Worked example:** upload a file:

```python
with open('report.pdf', 'rb') as f:
    r = requests.post(
        'https://api.example.com/upload',
        files={'file': ('report.pdf', f, 'application/pdf')},
        headers={'Authorization': 'Bearer TOKEN'},
        timeout=30,
    )
    r.raise_for_status()
```

## Query parameters

Pass `params=` as a dict — requests builds and encodes the query string:

```python
requests.get(
    'https://api.example.com/search',
    params={'q': 'python', 'page': 2, 'sort': 'newest'},
    timeout=10,
)
# GET https://api.example.com/search?q=python&page=2&sort=newest
```

Never hand-build query strings with user input — special characters need URL encoding that `params=` handles automatically.

## Building requests without sending

Great for unit tests of URL construction — no network, no mocks needed for the URL part:

```python
from requests import Request, Session

req = Request('GET', 'https://api.example.com/search', params={'q': 'py'})
prepared = Session().prepare_request(req)
assert prepared.method == 'GET'
assert 'q=py' in prepared.url
```

**Worked example:** helper that builds a search URL:

```python
def prepare_search(base: str, query: str, page: int = 1) -> str:
    req = Request('GET', base, params={'q': query, 'page': page})
    return Session().prepare_request(req).url

url = prepare_search('https://shop.example/api/items', 'blue socks', page=3)
# https://shop.example/api/items?q=blue+socks&page=3
```

**Worked example:** inspect headers before sending:

```python
def build_auth_request(url: str, token: str) -> requests.PreparedRequest:
    req = Request('GET', url, headers={'Authorization': f'Bearer {token}'})
    return Session().prepare_request(req)

prepared = build_auth_request('https://api.example.com/me', 'secret')
assert prepared.headers['Authorization'] == 'Bearer secret'
```

## Real-world scenario: GitHub API call

```python
import os
import requests

TOKEN = os.environ['GITHUB_TOKEN']  # never hard-code secrets

def list_repos(owner: str) -> list[dict]:
    r = requests.get(
        f'https://api.github.com/users/{owner}/repos',
        headers={'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/vnd.github+json'},
        params={'sort': 'updated', 'per_page': 10},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()
```

## Sessions

A `Session` reuses TCP connections and persists cookies/headers:

```python
with requests.Session() as s:
    s.headers.update({'User-Agent': 'myapp/1.0'})
    s.get('https://api.example.com/page1', timeout=10)
    s.get('https://api.example.com/page2', timeout=10)
    # second call reuses the connection — faster
```

Use a session when calling the same host repeatedly.

## Downloading large files

```python
with requests.get(url, stream=True, timeout=30) as r:
    r.raise_for_status()
    with open('output.bin', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
```

`stream=True` avoids loading the entire file into memory.

## Error handling pattern

```python
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
except requests.Timeout:
    print('server too slow')
except requests.HTTPError as e:
    print(f'HTTP error: {e.response.status_code}')
except requests.JSONDecodeError:
    print('response was not JSON')
except requests.RequestException as e:
    print(f'network problem: {e}')
```

Do not call `.json()` until you know the response succeeded and is JSON.

## Common pitfalls

- No timeout → hung workers forever
- Trusting `response.json()` without checking status (500 pages are often HTML)
- Sending secrets in query strings (logged in proxies, browser history, server logs)
- Hard-coding URLs and API keys — use environment variables or config files
- Ignoring rate limits (HTTP 429) — back off and respect `Retry-After`
- Not handling redirects explicitly when POSTing (use `allow_redirects=False` to inspect 302 responses)

## Practice

Build a prepared GET request with query parameters.

## Summary

requests = ergonomic HTTP for sync Python. Use `get`/`post` with `timeout`, check status with `raise_for_status()`, parse JSON only on success. Test URL building with `Request` + `Session().prepare_request()`; use `Session` for repeated calls to the same API.
