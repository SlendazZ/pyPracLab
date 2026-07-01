from fastapi import FastAPI, HTTPException

def create_app():
    app = FastAPI()
    @app.get('/items/{item_id}')
    def read(item_id: int):
        if item_id == 0:
            raise HTTPException(status_code=404)
        return {'item_id': item_id}
    return app
