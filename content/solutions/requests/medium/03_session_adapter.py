import requests

def make_session():
    s = requests.Session()
    s.headers['User-Agent'] = 'pyprac/1.0'
    return s
