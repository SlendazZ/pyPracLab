from requests import Request

def build_clean(url: str, params: dict):
    clean = {k: v for k, v in params.items() if v is not None}
    return Request('GET', url, params=clean).prepare()
