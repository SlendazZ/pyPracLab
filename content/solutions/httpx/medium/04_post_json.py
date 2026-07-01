import httpx

def post_json(url: str, payload: dict):
    return httpx.Request('POST', url, json=payload)
