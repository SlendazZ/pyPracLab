from fastapi import FastAPI
from pydantic import BaseModel

def create_app():
    app = FastAPI()
    class UserOut(BaseModel):
        id: int
        name: str
    @app.get('/user', response_model=UserOut)
    def user():
        return {'id': 1, 'name': 'eli', 'secret': 'shh'}
    return app
