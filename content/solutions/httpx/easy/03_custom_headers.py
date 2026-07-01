import httpx

def build_with_headers(url: str, headers: dict):
    return httpx.Request('GET', url, headers=headers)
