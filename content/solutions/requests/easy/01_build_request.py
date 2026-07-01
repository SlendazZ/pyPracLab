from requests import Request

def build_request(method: str, url: str, params: dict):
    return Request(method, url, params=params).prepare()
