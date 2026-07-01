import httpx

def patch_json(url: str, payload: dict):
    return httpx.Request('PATCH', url, json=payload)
