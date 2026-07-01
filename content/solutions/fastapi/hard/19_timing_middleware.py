def register(app) -> None:
    @app.middleware('http')
    async def add_header(request, call_next):
        response = await call_next(request)
        response.headers['X-Processed'] = '1'
        return response
