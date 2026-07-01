---
title: REST API Design Basics
track: apis
difficulty: medium
tags: rest, api-design
exercise: content/problems/apis/medium/12_merge_query_params.py
---

# REST API Design Basics

## Overview

REST (Representational State Transfer) organizes APIs around resources (nouns) and HTTP verbs (actions). Good design is predictable: the same patterns everywhere.

When you read a well-designed API, you should guess the next endpoint before reading the docs: plural nouns, standard methods, consistent JSON shapes, and status codes that match what actually happened.

Bad APIs mix verbs into URLs, return 200 for everything, and rename fields between endpoints. Good APIs feel boring — in a good way.

## Resource-oriented URLs

Paths name *things*, not actions. HTTP methods carry the verb:

```
GET    /users          list users
POST   /users          create user
GET    /users/42       get user 42
PATCH  /users/42       update fields
DELETE /users/42       remove user
GET    /users/42/posts nested collection
```

Use plural nouns (`/users`, not `/user`). Avoid verbs in paths — `/getUser` and `/createOrder` fight the HTTP method model.

IDs identify one resource. Collections live at the plural path:

```
GET /items        → [{"id": 1, ...}, {"id": 2, ...}]
GET /items/7      → {"id": 7, ...}
```

Nested resources express ownership:

```
GET  /users/42/orders       list orders for user 42
POST /users/42/orders       create order for user 42
GET  /orders/99/items       line items on order 99
```

Do not nest more than two levels deep (`/a/b/c` is usually a smell).

## Status codes that match intent

Return the code that describes the outcome, not always 200:

- 200 OK — successful GET, PATCH, or PUT with a body
- 201 Created + `Location` header on POST
- 204 No Content on DELETE success (no body needed)
- 400 Bad Request for validation errors (bad JSON, missing field)
- 404 Not Found when the resource ID does not exist
- 409 Conflict for duplicate unique keys (email already taken)

Example POST response headers:

```
HTTP/1.1 201 Created
Location: /users/42
Content-Type: application/json

{"id": 42, "email": "ada@example.com"}
```

Worked example: choose the right code in a tiny handler:

```python
def delete_user(user_id: int, db: dict) -> tuple[int, str | None]:
    if user_id not in db:
        return 404, '{"error": "not_found"}'
    del db[user_id]
    return 204, None   # success, no body
```

## Request and response shapes

Keep field names consistent across every endpoint — pick snake_case or camelCase and stick with it:

```json
{
  "id": 42,
  "email": "ada@example.com",
  "created_at": "2026-01-15T10:00:00Z"
}
```

Timestamps as ISO-8601 strings (`2026-01-15T10:00:00Z`) parse cleanly in every language. Booleans are `true`/`false`, not `1`/`0`.

List responses wrap items plus metadata:

```json
{
  "items": [
    {"id": 1, "name": "Widget"},
    {"id": 2, "name": "Gadget"}
  ]
}
```

Error bodies should be machine- and human-readable:

```json
{
  "error": "validation_failed",
  "message": "email is required",
  "fields": {"email": "missing"}
}
```

## Pagination and filtering

List endpoints accept query parameters instead of new paths:

```
GET /items?limit=20&offset=40
GET /items?sort=-created_at&tag=python
GET /items?status=active&min_price=10
```

Return metadata so clients know how to fetch the next page:

```json
{
  "items": [...],
  "total": 150,
  "limit": 20,
  "offset": 40
}
```

Client logic for paging through all results:

```python
def fetch_all_items(client, base_url: str, limit: int = 50) -> list[dict]:
    offset = 0
    all_items = []
    while True:
        url = f'{base_url}?limit={limit}&offset={offset}'
        page = client.get(url).json()
        all_items.extend(page['items'])
        offset += limit
        if offset >= page['total']:
            break
    return all_items
```

## Worked example: merge and build query strings

Clients often combine default filters with user-supplied ones. Merge dicts, then encode safely:

```python
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse

def merge_query_params(url: str, extra: dict) -> str:
    parts = urlparse(url)
    existing = {k: v[0] for k, v in parse_qs(parts.query).items()}
    merged = {**existing, **extra}
    new_query = urlencode(merged)
    return urlunparse(parts._replace(query=new_query))

base = 'https://api.example.com/items?limit=20&tag=python'
merged = merge_query_params(base, {'page': 2, 'tag': 'api'})
# tag=api overwrites tag=python; page=2 is added
```

Step by step:
1. `urlparse` splits the URL into components.
2. `parse_qs` reads existing query keys (values are lists).
3. Dict merge lets new params override old ones.
4. `urlencode` + `urlunparse` rebuilds a valid URL.

Trace the merge:

```python
print(merged)
# https://api.example.com/items?limit=20&tag=api&page=2
```

For greenfield URLs without existing params:

```python
from urllib.parse import urlencode

def build_list_url(base: str, **filters) -> str:
    clean = {k: v for k, v in filters.items() if v is not None}
    if not clean:
        return base
    return f'{base}?{urlencode(clean)}'

build_list_url('https://api.example.com/items', limit=20, tag='python')
# https://api.example.com/items?limit=20&tag=python
build_list_url('https://api.example.com/items', limit=20, tag=None)
# https://api.example.com/items?limit=20  — None keys dropped
```

## Idempotency and method choice

GET, PUT, and DELETE should be safe to repeat — calling them twice should not create duplicate side effects. POST creates new resources each time.

```
GET    /items/7     → read (safe, repeatable)
PUT    /items/7     → replace entire resource
PATCH  /items/7     → change one field
POST   /items       → create (each call may add another row)
```

Use PATCH for partial updates (`{"email": "new@x.com"}`), PUT when the client sends the full resource representation.

## Versioning and errors

- Prefix: `/v1/users` or header `Accept: application/vnd.myapp.v1+json`
- Bump version when you remove or rename fields — clients depend on stability
- Never return stack traces in 500 responses; log them server-side

## Common pitfalls

- Using POST for everything (including idempotent reads)
- Leaking internal IDs or stack traces in 500 responses
- Breaking changes without version bump
- Inconsistent pluralization (`/user` vs `/users`)
- Pagination without total count or next-page link
- Encoding query params by hand — spaces and `&` break URLs

## Practice

Build query strings for filter parameters safely with urlencode.

## Summary

REST = resources + HTTP semantics + consistent JSON. Design for the client you wish you had when reading someone else's API: predictable URLs, honest status codes, and query strings built with `urlencode`, not string concat.
