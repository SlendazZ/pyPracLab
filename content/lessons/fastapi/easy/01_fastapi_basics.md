---
title: FastAPI Basics
track: fastapi
difficulty: easy
tags: fastapi, http
exercise: content/problems/fastapi/easy/01_hello_route.py
---

# FastAPI Basics

## Overview

FastAPI is a modern Python web framework for building APIs. It uses type hints for automatic validation, generates interactive OpenAPI docs, and runs on ASGI servers like Uvicorn (async-capable, high performance).

You write ordinary Python functions with type annotations; FastAPI turns them into HTTP endpoints with JSON request/response handling.

Real-world uses:

- REST backends for web and mobile apps
- Internal microservices behind a gateway
- Webhook receivers (Stripe, GitHub, Slack)
- ML model serving endpoints

Install with `pip install fastapi uvicorn`.

## Minimal app

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'hello'}
```

Return dicts, lists, or Pydantic models — FastAPI serializes them to JSON automatically. You do not need to call `json.dumps()` yourself.

Run locally:

```bash
uvicorn main:app --reload
```

- `main` = Python file name (`main.py`)
- `app` = the FastAPI instance variable
- `--reload` = restart on code changes (development only)

Open `http://127.0.0.1:8000/docs` for Swagger UI — try endpoints in the browser. `/redoc` is an alternative docs view.

## Path and query parameters

Path segments in `{braces}` and function parameters share names:

```python
@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}
```

```bash
GET /items/42?q=python
# → {"item_id": 42, "q": "python"}

GET /items/not-a-number
# → 422 Unprocessable Entity with field-level error details
```

Types in the signature drive parsing and validation. FastAPI rejects bad input before your function body runs.

Optional query params use `None` as default:

```python
@app.get('/search')
def search(q: str, page: int = 1, limit: int = 20):
    return {'q': q, 'page': page, 'limit': limit}
```

## HTTP methods

```python
@app.get('/items')       # read list
@app.get('/items/{id}') # read one
@app.post('/items')      # create
@app.put('/items/{id}')  # replace
@app.patch('/items/{id}')# partial update
@app.delete('/items/{id}')# remove
```

## Request body (preview)

POST/PATCH routes accept JSON bodies via Pydantic models (covered in the next lesson). For now, know that FastAPI reads the body, validates it, and passes a Python object to your handler.

## Status codes and responses

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.post('/items', status_code=status.HTTP_201_CREATED)
def create_item():
    return {'id': 1}

@app.get('/items/{item_id}')
def get_item(item_id: int):
    if item_id == 404:
        raise HTTPException(status_code=404, detail='Item not found')
    return {'id': item_id}
```

Use `status_code=` on the decorator for non-200 defaults. `HTTPException` returns JSON like `{"detail": "..."}`.

## Testing without a live server

`TestClient` runs the app in-process — no port, no network flake:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'hello'}

def test_item_with_query():
    response = client.get('/items/7?q=test')
    assert response.status_code == 200
    assert response.json()['item_id'] == 7
```

**Worked example:** test validation failure:

```python
def test_invalid_item_id():
    response = client.get('/items/abc')
    assert response.status_code == 422
    detail = response.json()['detail']
    assert any('item_id' in str(err.get('loc', [])) for err in detail)
```

**Worked example:** test 404:

```python
def test_missing_item():
    response = client.get('/items/404')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Item not found'
```

Always prefer `TestClient` in unit tests over `requests.get('localhost:8000')`.

## Sync vs async routes

```python
@app.get('/fast')
def sync_route():
    return {'ok': True}

@app.get('/async')
async def async_route():
    return {'ok': True}
```

Use `async def` when you `await` non-blocking I/O (httpx.AsyncClient, async database drivers). Do not put blocking calls (`time.sleep`, sync `requests.get`) inside `async def` — they block the event loop. Either use sync `def` or run blocking code in a thread pool.

## Real-world scenario: health check endpoint

```python
from datetime import datetime, timezone

@app.get('/health')
def health():
    return {
        'status': 'ok',
        'timestamp': datetime.now(timezone.utc).isoformat(),
    }
```

Load balancers and Kubernetes probes call `/health` to verify the service is alive. Keep it fast — no heavy database queries.

## Project layout tips

```
app/
  main.py          # app = FastAPI(); include routers
  routers/
    users.py       # APIRouter(prefix='/users')
  models.py        # Pydantic schemas
  settings.py      # env-based config
```

Split routers to keep files small:

```python
from fastapi import APIRouter
router = APIRouter()

@router.get('/')
def list_users():
    return []

# in main.py:
app.include_router(router, prefix='/users', tags=['users'])
```

Load settings from environment variables (pydantic-settings or `os.environ`).

## Common pitfalls

- Returning non-JSON-serializable objects (datetime without conversion, custom classes)
- Blocking I/O in `async def` routes
- Testing with real HTTP when TestClient suffices
- Forgetting `--reload` is dev-only; use a process manager in production
- Putting business logic directly in route functions — extract services as the app grows
- Defining routes after `uvicorn` starts — import order matters

## Practice

Create a GET `/` route that returns a greeting JSON object.

## Summary

FastAPI = typed routes + automatic validation + OpenAPI docs + easy testing. Define `app = FastAPI()`, decorate handlers with `@app.get`/`@app.post`, return dicts, and verify behavior with `TestClient` before deploying.
