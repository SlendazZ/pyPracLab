import httpx

def delete_request(url: str):
    return httpx.Request('DELETE', url)
