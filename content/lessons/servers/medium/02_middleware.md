---
title: Middleware and Request Lifecycle
track: servers
difficulty: medium
tags: middleware, wsgi
exercise: content/problems/servers/easy/10_request_log_line.py
---

# Middleware and Request Lifecycle

## Overview

Middleware wraps request handling to add cross-cutting behavior: logging, authentication, CORS headers, compression, error pages. Each layer calls the next inner layer.

Handlers should focus on business logic (create user, fetch order). Middleware handles concerns that apply to *many* routes — things you do not want to copy-paste into every handler.

Imagine peeling an onion: the request travels inward through layers until it reaches your handler, then the response travels back out through the same layers in reverse order.

## Onion model

Picture nested wrappers. The request enters from the outside; the response unwinds back out:

```
Request  → [Logging] → [Auth] → [Router] → Handler
Response ← [Logging] ← [Auth] ← [Router] ← Handler
```

Outer middleware sees the request first and the response last. That is why logging middleware can record total time including inner layers.

Order matters:

```
1. Error handler (outermost — catches exceptions from everything inside)
2. Logging / timing
3. CORS (before response leaves)
4. Authentication (attach user to request)
5. Router + handler (innermost)
```

## Simple WSGI-style wrapper

WSGI apps are callables `(environ, start_response) -> iterable`. Middleware is a function that takes an app and returns a new app:

```python
def logging_middleware(app):
    def wrapper(environ, start_response):
        method = environ.get('REQUEST_METHOD', 'GET')
        path = environ.get('PATH_INFO', '/')
        print(f'{method} {path}')
        return app(environ, start_response)
    return wrapper
```

Stack middleware by nesting — outermost runs first on the way in:

```python
app = logging_middleware(timing_middleware(core_app))
```

Reading the stack right-to-left: `core_app` is innermost; `logging_middleware` wraps everything and runs first when a request arrives.

## Worked example: request log line with timing

A practical logger records method, path, status, and duration:

```python
import time

def request_log_middleware(app):
    def wrapper(environ, start_response):
        start = time.perf_counter()
        method = environ.get('REQUEST_METHOD', 'GET')
        path = environ.get('PATH_INFO', '/')
        status_holder = []

        def custom_start_response(status, headers, exc_info=None):
            status_holder.append(status)
            return start_response(status, headers, exc_info)

        try:
            result = app(environ, custom_start_response)
        finally:
            elapsed_ms = (time.perf_counter() - start) * 1000
            code = status_holder[0].split()[0] if status_holder else '???'
            print(f'{method} {path} {code} {elapsed_ms:.1f}ms')
        return result
    return wrapper
```

Step by step:
1. Record start time before calling the inner app.
2. Wrap `start_response` to capture the HTTP status code.
3. Call the inner app — it may be routing, auth, or the real handler.
4. In `finally`, log one line regardless of success or exception.

Example output: `GET /health 200 1.3ms`

Why wrap `start_response`? The inner app chooses the status (200, 404, 500). Middleware that only logs before calling the inner app would not know the final status.

## Worked example: add a response header

Middleware can modify headers on the way out:

```python
def security_headers_middleware(app):
    def wrapper(environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            headers = list(headers)
            headers.append(('X-Content-Type-Options', 'nosniff'))
            return start_response(status, headers, exc_info)
        return app(environ, custom_start_response)
    return wrapper
```

Every response now includes `X-Content-Type-Options: nosniff` without touching individual handlers.

## Worked example: global exception handler

Convert uncaught errors into JSON 500 responses:

```python
import json

def error_middleware(app):
    def wrapper(environ, start_response):
        try:
            return app(environ, start_response)
        except Exception:
            body = json.dumps({'error': 'internal_server_error'}).encode()
            start_response('500 Internal Server Error', [
                ('Content-Type', 'application/json'),
                ('Content-Length', str(len(body))),
            ])
            return [body]
    return wrapper
```

Place this outermost so it catches failures from auth, routing, and handlers.

## ASGI (async) equivalent

Modern async frameworks use ASGI. The shape is the same — wrap the inner app — but with `async def` and `scope`, `receive`, `send`:

```python
class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            method = scope['method']
            path = scope['path']
            print(f'{method} {path}')
        await self.app(scope, receive, send)
```

FastAPI and Starlette build on this pattern. The wrapping idea is identical to WSGI — only the callable signature changes.

## What belongs in middleware

- Request/response logging with timing
- Adding security headers (`X-Content-Type-Options`, etc.)
- Session cookie parsing (attach user to request context)
- Global exception → JSON error mapping
- CORS headers for browser clients

## What does NOT belong

- Business logic specific to one route (put that in the handler)
- Heavy DB queries per request without caching
- Parsing request bodies for a single endpoint

## Stacking middleware: full example

```python
def build_app(core):
  app = core
  app = security_headers_middleware(app)
  app = request_log_middleware(app)
  app = error_middleware(app)   # outermost
  return app
```

Each line wraps the previous `app`. The last wrapper added is the first to see incoming requests.

## Common pitfalls

- Middleware that forgets to call the inner app — requests hang forever
- Swallowing exceptions without re-raising or converting to 500 JSON
- Wrong order: CORS must run early; auth before handlers that need identity
- Mutating global state per request without thread/async safety
- Logging bodies with passwords or API keys
- Forgetting to return the inner app's iterable (WSGI) or await it (ASGI)

## Practice

Build a request logger that records method and path.

## Summary

Middleware composes behavior around handlers. Keep each layer focused; order matters. Wrap the inner app, always call through, and use the onion model to decide what runs before routing versus after the handler returns.
