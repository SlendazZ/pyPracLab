def register(app) -> None:
    @app.patch('/items/{item_id}')
    def patch_item(item_id: int, body: dict):
        return {'id': item_id, 'name': body['name']}
