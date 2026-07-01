import httpx

def build_request(method: str, url: str):
    return httpx.Request(method, url)
