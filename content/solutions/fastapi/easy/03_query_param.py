from fastapi import FastAPI

def create_app():
    app = FastAPI()
    @app.get('/search')
    def search(q: str = ''):
        return {"q": q}
    return app
