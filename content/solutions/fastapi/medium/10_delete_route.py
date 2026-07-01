def register(app) -> None:
    @app.delete('/items/{item_id}', status_code=204)
    def delete_item(item_id: int):
        return None
