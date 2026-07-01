def route(routes: dict, method: str, path: str) -> str:
    return routes.get((method, path), 'not_found')
