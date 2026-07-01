from fastapi import FastAPI

def create_app():
    app = FastAPI()
    @app.get('/')
    def root():
        return {"message": "hello"}
    @app.get('/health')
    def health():
        return {"status": "ok"}
    return app
