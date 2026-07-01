"""FastAPI problem specs."""

PROBLEMS = [
    {
        "slug": "01_hello_route",
        "track": "fastapi", "difficulty": "easy",
        "title": "FastAPI Hello Route",
        "tags": ["fastapi", "http"],
        "description": "Create and return a FastAPI app with GET '/' returning {\"message\": \"hello\"} and GET '/health' returning {\"status\": \"ok\"}.",
        "examples": "create_app() testable with TestClient",
        "hint": "from fastapi import FastAPI; app = FastAPI(); use @app.get.",
        "syntax_hint": '@app.get("/") def root(): return {"message": "hello"}',
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    r = client.get('/')\n"
            "    assert r.status_code == 200\n"
            "    assert r.json() == {\"message\": \"hello\"}\n"
            "    assert client.get('/health').json() == {\"status\": \"ok\"}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    @app.get('/')\n"
            "    def root():\n"
            "        return {\"message\": \"hello\"}\n"
            "    @app.get('/health')\n"
            "    def health():\n"
            "        return {\"status\": \"ok\"}\n"
            "    return app\n"
        ),
    },
    {
        "slug": "02_path_param",
        "track": "fastapi", "difficulty": "easy",
        "title": "Path Parameter",
        "tags": ["fastapi", "http"],
        "description": "Create an app with GET '/items/{item_id}' returning {\"item_id\": item_id} (as an int).",
        "examples": "GET /items/42 -> {\"item_id\": 42}",
        "hint": "Declare the path param with a Python type annotation to get conversion.",
        "syntax_hint": 'def read(item_id: int): return {"item_id": item_id}',
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    r = client.get('/items/42')\n"
            "    assert r.status_code == 200\n"
            "    assert r.json() == {\"item_id\": 42}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    @app.get('/items/{item_id}')\n"
            "    def read(item_id: int):\n"
            "        return {\"item_id\": item_id}\n"
            "    return app\n"
        ),
    },
    {
        "slug": "03_query_param",
        "track": "fastapi", "difficulty": "easy",
        "title": "Query Parameters",
        "tags": ["fastapi", "http"],
        "description": "Create an app with GET '/search' that takes a 'q' query param and returns {\"q\": q}. Use a default of empty string.",
        "examples": "GET /search?q=py -> {\"q\": \"py\"}",
        "hint": "Function parameters with defaults become query params.",
        "syntax_hint": 'def search(q: str = ""): return {"q": q}',
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    assert client.get('/search?q=py').json() == {\"q\": \"py\"}\n"
            "    assert client.get('/search').json() == {\"q\": \"\"}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    @app.get('/search')\n"
            "    def search(q: str = ''):\n"
            "        return {\"q\": q}\n"
            "    return app\n"
        ),
    },
    {
        "slug": "04_post_body",
        "track": "fastapi", "difficulty": "medium",
        "title": "POST with a Pydantic Body",
        "tags": ["fastapi", "pydantic"],
        "description": "Create an app with POST '/echo' that accepts a Pydantic model {name: str, age: int} and returns it unchanged.",
        "examples": "POST /echo {name,age} -> same body",
        "hint": "Define a BaseModel and type the request body parameter.",
        "syntax_hint": "class Person(BaseModel): name: str; age: int",
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    r = client.post('/echo', json={'name': 'eli', 'age': 30})\n"
            "    assert r.status_code == 200\n"
            "    assert r.json() == {'name': 'eli', 'age': 30}\n"
            "    assert client.post('/echo', json={'name': 'eli'}).status_code == 422\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    class Person(BaseModel):\n"
            "        name: str\n"
            "        age: int\n"
            "    @app.post('/echo')\n"
            "    def echo(person: Person):\n"
            "        return person\n"
            "    return app\n"
        ),
    },
    {
        "slug": "05_status_codes",
        "track": "fastapi", "difficulty": "medium",
        "title": "Custom Status Codes",
        "tags": ["fastapi", "http"],
        "description": "Create an app with POST '/create' that returns status 201 and {\"created\": True}.",
        "examples": "POST /create -> 201 {\"created\": true}",
        "hint": "from fastapi import status; use status_code=status.HTTP_201_CREATED.",
        "syntax_hint": "@app.post('/create', status_code=status.HTTP_201_CREATED)",
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    r = client.post('/create')\n"
            "    assert r.status_code == 201\n"
            "    assert r.json() == {\"created\": True}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI, status\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    @app.post('/create', status_code=status.HTTP_201_CREATED)\n"
            "    def create():\n"
            "        return {\"created\": True}\n"
            "    return app\n"
        ),
    },
    {
        "slug": "06_response_model",
        "track": "fastapi", "difficulty": "medium",
        "title": "Response Model Filtering",
        "tags": ["fastapi", "pydantic"],
        "description": "Create an app with GET '/user' returning a UserOut model {id, name} from internal data that also has a 'secret' field; the secret must NOT be in the response.",
        "examples": "GET /user -> {\"id\":1,\"name\":\"eli\"} (no secret)",
        "hint": "Use response_model=UserOut on the route to filter fields.",
        "syntax_hint": "@app.get('/user', response_model=UserOut)",
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    r = client.get('/user')\n"
            "    assert r.status_code == 200\n"
            "    body = r.json()\n"
            "    assert body == {'id': 1, 'name': 'eli'}\n"
            "    assert 'secret' not in body\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    class UserOut(BaseModel):\n"
            "        id: int\n"
            "        name: str\n"
            "    @app.get('/user', response_model=UserOut)\n"
            "    def user():\n"
            "        return {'id': 1, 'name': 'eli', 'secret': 'shh'}\n"
            "    return app\n"
        ),
    },
    {
        "slug": "07_dependency",
        "track": "fastapi", "difficulty": "hard",
        "title": "Dependency Injection",
        "tags": ["fastapi", "di"],
        "description": "Create an app using a dependency that reads the 'X-User' header; GET '/me' returns {\"user\": <header or 'anonymous'>}.",
        "examples": "GET /me with X-User: eli -> {\"user\": \"eli\"}",
        "hint": "Define def get_user(x_user: str = Header(default='anonymous')) and Depends() it.",
        "syntax_hint": "from fastapi import Header, Depends",
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    assert client.get('/me').json() == {'user': 'anonymous'}\n"
            "    assert client.get('/me', headers={'X-User': 'eli'}).json() == {'user': 'eli'}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI, Header, Depends\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    def get_user(x_user: str = Header(default='anonymous')):\n"
            "        return x_user\n"
            "    @app.get('/me')\n"
            "    def me(user: str = Depends(get_user)):\n"
            "        return {'user': user}\n"
            "    return app\n"
        ),
    },
    {
        "slug": "08_exception_handler",
        "track": "fastapi", "difficulty": "medium",
        "title": "HTTPException",
        "tags": ["fastapi", "errors"],
        "description": "Create an app with GET '/items/{item_id}' that raises HTTPException(404) when item_id is 0, else returns {\"item_id\": item_id}.",
        "examples": "GET /items/0 -> 404",
        "hint": "from fastapi import HTTPException; raise HTTPException(status_code=404).",
        "syntax_hint": "if item_id == 0: raise HTTPException(status_code=404)",
        "signature": "def create_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi.testclient import TestClient\n"
            "    client = TestClient(create_app())\n"
            "    assert client.get('/items/5').json() == {'item_id': 5}\n"
            "    assert client.get('/items/0').status_code == 404\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import FastAPI, HTTPException\n\n"
            "def create_app():\n"
            "    app = FastAPI()\n"
            "    @app.get('/items/{item_id}')\n"
            "    def read(item_id: int):\n"
            "        if item_id == 0:\n"
            "            raise HTTPException(status_code=404)\n"
            "        return {'item_id': item_id}\n"
            "    return app\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_fastapi_basics",
        "track": "fastapi", "difficulty": "easy",
        "title": "FastAPI Basics",
        "tags": ["fastapi", "http"],
        "exercise": "content/problems/fastapi/easy/01_hello_route.py",
        "body": (
            "# FastAPI Basics\n\n"
            "FastAPI turns Python functions into HTTP endpoints.\n\n"
            "```python\nfrom fastapi import FastAPI\napp = FastAPI()\n\n"
            "@app.get('/')\ndef root():\n    return {\"message\": \"hello\"}\n```\n\n"
            "## Testing without a server\n\n"
            "```python\nfrom fastapi.testclient import TestClient\n"
            "client = TestClient(app)\nassert client.get('/').json() == {\"message\": \"hello\"}\n```\n\n"
            "No port, no network — perfect for exercises."
        ),
    },
]
