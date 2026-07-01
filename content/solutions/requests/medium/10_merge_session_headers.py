def merge(session: dict, request: dict) -> dict:
    return {**session, **request}
