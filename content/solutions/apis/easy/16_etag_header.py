import hashlib

def make_etag(body: bytes) -> str:
    return f'"{hashlib.md5(body).hexdigest()}"'
