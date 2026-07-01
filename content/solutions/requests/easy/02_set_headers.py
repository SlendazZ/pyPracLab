from requests import Request

def build_with_headers(method: str, url: str, headers: dict):
    return Request(method, url, headers=headers).prepare()
