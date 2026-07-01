def register(app) -> None:
    @app.put('/items/{item_id}')
    def put_item(item_id: int, body: dict):
        return {'id': item_id, 'data': body}
