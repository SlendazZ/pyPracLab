---
title: Pydantic Models and Validation
track: fastapi
difficulty: medium
tags: pydantic, validation
exercise: content/problems/fastapi/medium/06_response_model.py
---

# Pydantic Models and Validation

## Overview

Pydantic models describe the shape of request and response data. FastAPI uses them to parse JSON bodies, validate fields, and generate OpenAPI schemas — your docs stay in sync with your code automatically.

Think of a Pydantic model as a contract: "this endpoint accepts exactly these fields, with these types and constraints."

## Defining a model

```python
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)
    age: int | None = None
```

Field constraints produce clear 422 errors when violated:

```json
{
  "detail": [
    {"loc": ["body", "email"], "msg": "value is not a valid email address"}
  ]
}
```

Common validators:

```python
from pydantic import Field

price: float = Field(gt=0, description='Must be positive')
tags: list[str] = Field(default_factory=list, max_length=10)
role: str = Field(pattern=r'^(admin|user|guest)$')
```

## Using models in routes

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    # user is already validated — safe to use
    return {'id': 1, **user.model_dump()}
```

Send JSON from a client or TestClient:

```python
client.post('/users', json={'email': 'ada@example.com', 'name': 'Ada'})
```

Invalid body → automatic 422 with per-field errors. Your handler never runs.

## Worked example: separate create and response shapes

Clients send passwords; responses should not echo them:

```python
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class UserOut(BaseModel):
    id: int
    email: EmailStr

@app.post('/users', response_model=UserOut, status_code=201)
def create_user(user: UserCreate):
    stored = save_user(user)  # hashes password internally
    return stored  # extra fields like password_hash are stripped
```

Even if `save_user` returns `password_hash`, `response_model=UserOut` filters it out of the JSON response.

## Response models

`response_model=` filters and validates what leaves your API:

```python
class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str

@app.get('/users/{uid}', response_model=UserOut)
def get_user(uid: int):
    row = db.get_user(uid)
    return row  # Pydantic drops extra keys, coerces types
```

This prevents accidentally leaking internal fields (`password_hash`, `internal_notes`) in JSON responses.

## model_dump and model_validate (Pydantic v2)

```python
user = UserCreate(email='a@b.com', name='Ada', password='long-enough')
data = user.model_dump()                    # dict for JSON/DB insert
safe = user.model_dump(exclude={'password'})  # omit sensitive fields
restored = UserCreate.model_validate({'email': 'a@b.com', 'name': 'Ada', 'password': 'long-enough'})
```

Pydantic v1 used `.dict()` and `.parse_obj()` — check your project's version in `requirements.txt` or `pyproject.toml`.

## Nested and optional models

```python
class Address(BaseModel):
    street: str
    city: str

class UserCreate(BaseModel):
    name: str
    address: Address | None = None
```

FastAPI validates nested objects recursively:

```python
client.post('/users', json={
    'name': 'Ada',
    'address': {'street': '1 Analytical Engine Rd', 'city': 'London'},
})
```

## Sharing fields with inheritance

```python
class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int
    model_config = {'from_attributes': True}
```

Create / Update / Out variants keep schemas DRY.

## Config for ORM objects

When returning SQLAlchemy or other ORM rows:

```python
class UserOut(BaseModel):
    model_config = {'from_attributes': True}
    id: int
    email: str
```

`from_attributes=True` lets Pydantic read attributes from arbitrary objects, not just dicts.

## Real-world scenario: webhook payload

```python
class StripeEvent(BaseModel):
    id: str
    type: str
    data: dict

@app.post('/webhooks/stripe')
def stripe_webhook(event: StripeEvent):
    if event.type == 'payment_intent.succeeded':
        handle_payment(event.data)
    return {'received': True}
```

Pydantic rejects malformed webhooks before your handler processes them.

## Testing validation

```python
def test_create_user_ok():
    r = client.post('/users', json={'email': 'ada@ex.com', 'name': 'Ada', 'password': 'secret123'})
    assert r.status_code == 201
    body = r.json()
    assert 'password' not in body

def test_create_user_bad_email():
    r = client.post('/users', json={'email': 'not-email', 'name': 'Ada', 'password': 'secret123'})
    assert r.status_code == 422

def test_create_user_short_password():
    r = client.post('/users', json={'email': 'ada@ex.com', 'name': 'Ada', 'password': 'short'})
    assert r.status_code == 422
```

## Common pitfalls

- Mutable defaults on model fields — use `Field(default_factory=list)` for lists/dicts
- Returning ORM objects without `from_attributes=True`
- One giant model for everything — split Create/Update/Out variants
- Validating the same rules in the route *and* the model (DRY violation)
- Forgetting `response_model` and leaking sensitive columns
- Using Pydantic v1 methods (`.dict()`) in a v2 project

## Practice

Define a User model with email and name validation.

## Summary

Pydantic = schema + validation + serialization. Define input models for request bodies, output models with `response_model` for responses, and share base fields via inheritance or composition. FastAPI + Pydantic turn type hints into live API contracts.
