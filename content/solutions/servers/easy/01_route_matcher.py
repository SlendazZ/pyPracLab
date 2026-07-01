def match(routes: dict[str, str], path: str) -> str:
    return routes.get(path, 'not_found')
