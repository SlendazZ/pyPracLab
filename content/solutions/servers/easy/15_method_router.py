def route_method(handlers: dict[str, str], method: str) -> str:
    return handlers.get(method.upper(), 'not_found')
