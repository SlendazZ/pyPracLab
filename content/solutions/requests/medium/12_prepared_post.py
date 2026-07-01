from requests import Request, Session

def prepare_post(url: str, data: dict):
    req = Request('POST', url, data=data)
    return Session().prepare_request(req)
