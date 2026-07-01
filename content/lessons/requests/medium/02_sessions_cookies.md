---
title: Sessions, Cookies, and Retries
track: requests
difficulty: medium
tags: session, cookies
exercise: content/problems/requests/easy/02_set_headers.py
---

# Sessions, Cookies, and Retries

## Overview

A `requests.Session` is a persistent client: it keeps headers, cookies, and TCP connections across multiple requests. Use it whenever you talk to the same host more than once — it is faster and mirrors how browsers work.

Real-world uses:

- Authenticated API clients (Bearer token on every call)
- Cookie-based login flows (session ID after POST /login)
- Scraping sites that set cookies on first visit
- Resilient integrations that retry transient 502/503 errors

## Default headers on a session

```python
import requests

session = requests.Session()
session.headers['Authorization'] = f'Bearer {token}'
session.headers['Accept'] = 'application/json'
session.headers['User-Agent'] = 'myapp/2.1'

r = session.get('https://api.example.com/me', timeout=10)
```

Per-request headers merge with session defaults. A call-level header overrides the session value for that request only:

```python
session.get(url, headers={'X-Request-Id': 'abc-123'}, timeout=10)
```

**Worked example:** API client class:

```python
class ApiClient:
    def __init__(self, base_url: str, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
        })
        self.base_url = base_url.rstrip('/')

    def get_user(self, user_id: int) -> dict:
        r = self.session.get(f'{self.base_url}/users/{user_id}', timeout=10)
        r.raise_for_status()
        return r.json()

    def create_user(self, payload: dict) -> dict:
        r = self.session.post(f'{self.base_url}/users', json=payload, timeout=10)
        r.raise_for_status()
        return r.json()
```

## Cookies

Sessions include a cookie jar that mimics browser behavior:

```python
session = requests.Session()

# login — server responds with Set-Cookie
session.post(
    'https://app.example.com/login',
    json={'user': 'ada', 'pass': '...'},
    timeout=10,
)

# subsequent requests send the session cookie automatically
dashboard = session.get('https://app.example.com/dashboard', timeout=10)
dashboard.raise_for_status()
```

Set cookies manually when needed:

```python
session.cookies.set('session_id', 'abc123', domain='app.example.com')
```

Inspect cookies: `session.cookies.get_dict()`.

**Worked example:** two-step auth flow:

```python
def authenticated_session(username: str, password: str) -> requests.Session:
    s = requests.Session()
    r = s.post('https://app.example.com/login', json={'user': username, 'pass': password}, timeout=10)
    r.raise_for_status()
    return s  # cookie jar now holds session token
```

## Retries with urllib3

Transient server errors (502, 503, 504) often resolve on retry. Mount a retry adapter on the session:

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[502, 503, 504],
    allowed_methods=['GET', 'HEAD', 'OPTIONS'],
)
adapter = HTTPAdapter(max_retries=retry)
session = requests.Session()
session.mount('https://', adapter)
session.mount('http://', adapter)
```

`backoff_factor=0.5` waits 0.5s, 1s, 2s between retries. **Retry POST carefully** — a succeeded request that timed out on the client can cause duplicates if you retry blindly. Use idempotency keys for payment APIs.

## Handling rate limits (429)

```python
import time

def get_with_backoff(session, url, max_retries=3):
    for attempt in range(max_retries):
        r = session.get(url, timeout=10)
        if r.status_code != 429:
            r.raise_for_status()
            return r
        wait = int(r.headers.get('Retry-After', 2 ** attempt))
        time.sleep(wait)
    raise RuntimeError('rate limited after retries')
```

## Context manager

```python
with requests.Session() as s:
    s.headers['Authorization'] = f'Bearer {token}'
    s.get(url1, timeout=10)
    s.get(url2, timeout=10)
# connections closed cleanly
```

One session per worker thread. Do not share a single Session across threads without care (urllib3 connection pool is not fully thread-safe for all usage patterns).

## Testing sessions

Test header merging logic directly without network:

```python
def build_session_headers(token: str) -> dict:
    s = requests.Session()
    s.headers['Authorization'] = f'Bearer {token}'
    s.headers['Accept'] = 'application/json'
    return dict(s.headers)

assert build_session_headers('tok')['Authorization'] == 'Bearer tok'
```

For full HTTP mocking, use `responses` or `requests-mock` in pytest:

```python
import responses

@responses.activate
def test_get_user():
    responses.add(responses.GET, 'https://api.test/users/1',
                  json={'name': 'Ada'}, status=200)
    client = ApiClient('https://api.test', 'fake-token')
    assert client.get_user(1)['name'] == 'Ada'

@responses.activate
def test_create_user():
    responses.add(responses.POST, 'https://api.test/users',
                  json={'id': 42, 'name': 'Grace'}, status=201)
    client = ApiClient('https://api.test', 'fake-token')
    result = client.create_user({'name': 'Grace'})
    assert result['id'] == 42
```

## Real-world scenario: paginated API with session

```python
def fetch_all_users(client: ApiClient) -> list[dict]:
    users = []
    page = 1
    while True:
        r = client.session.get(
            f'{client.base_url}/users',
            params={'page': page, 'limit': 100},
            timeout=10,
        )
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        users.extend(batch)
        page += 1
    return users
```

## Common pitfalls

- Creating a new `Session()` per request (loses pooling and cookie benefits)
- Retrying POST on 500 without idempotency keys
- Storing session tokens in committed files (`cookies.txt`, `.env` in git)
- Forgetting to set timeouts on session requests too
- Assuming cookies persist after `Session` is closed — save tokens explicitly if you need them later
- Not checking `Retry-After` on 429 responses

## Practice

Configure a session with shared auth headers.

## Summary

Session = persistent client state across requests. Configure default headers once, let cookies flow automatically, mount retry adapters for transient errors on safe methods, and use one session per logical client (per thread or async worker).
