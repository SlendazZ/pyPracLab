from fastapi.responses import JSONResponse

def register(app) -> None:
    @app.get('/data')
    def data():
        return JSONResponse({'ok': True}, headers={'X-Custom': 'yes'})
