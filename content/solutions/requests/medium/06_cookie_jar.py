import requests

def make_session_with_cookies(cookies: dict):
    s = requests.Session()
    s.cookies.update(cookies)
    return s
