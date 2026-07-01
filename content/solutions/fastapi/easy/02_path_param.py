from fastapi import FastAPI

def create_app():
    app = FastAPI()
    @app.get('/items/{item_id}')
    def read(item_id: int):
        return {"item_id": item_id}
    return app
