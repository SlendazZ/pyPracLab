from fastapi import FastAPI
from pydantic import BaseModel

def create_app():
    app = FastAPI()
    class Person(BaseModel):
        name: str
        age: int
    @app.post('/echo')
    def echo(person: Person):
        return person
    return app
