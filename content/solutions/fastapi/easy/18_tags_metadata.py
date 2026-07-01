def register(app) -> None:
    @app.get('/pets', tags=['animals'])
    def pets():
        return {'pets': []}
