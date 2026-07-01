from fastapi import Header, HTTPException

def register(app) -> None:
    @app.get('/secure')
    def secure(x_api_key: str = Header(default='')):
        if x_api_key != 'secret':
            raise HTTPException(status_code=401)
        return {'ok': True}
