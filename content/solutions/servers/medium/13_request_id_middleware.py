def add_request_id(headers: dict, rid: str) -> dict:
    h = dict(headers)
    h.setdefault('X-Request-Id', rid)
    return h
