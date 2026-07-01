import requests

def session_no_env():
    s = requests.Session()
    s.trust_env = False
    return s
