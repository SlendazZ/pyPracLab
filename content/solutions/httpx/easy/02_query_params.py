import httpx

def build_with_params(url: str, params: dict):
    return httpx.Request('GET', url, params=params)
