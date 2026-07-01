from fastapi import FastAPI, Header, Depends

def create_app():
    app = FastAPI()
    def get_user(x_user: str = Header(default='anonymous')):
        return x_user
    @app.get('/me')
    def me(user: str = Depends(get_user)):
        return {'user': user}
    return app
