def register(app) -> None:
    @app.get('/search')
    def search(q: str = ''):
        return {'q': q}
