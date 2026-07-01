from fastapi import FastAPI, status

def create_app():
    app = FastAPI()
    @app.post('/create', status_code=status.HTTP_201_CREATED)
    def create():
        return {"created": True}
    return app
