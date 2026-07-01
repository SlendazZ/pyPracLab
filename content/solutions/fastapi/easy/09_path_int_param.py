def register(app) -> None:
    @app.get('/items/{item_id}')
    def get_item(item_id: int):
        return {'id': item_id}
