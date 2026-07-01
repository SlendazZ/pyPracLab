from urllib.parse import parse_qs
from starlette.requests import Request

def register(app) -> None:
    @app.post('/login')
    async def login(request: Request):
        body = await request.body()
        data = parse_qs(body.decode())
        return {'user': data.get('username', [''])[0]}
