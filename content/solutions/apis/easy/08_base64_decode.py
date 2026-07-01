import base64

def decode(s: str) -> bytes:
    return base64.b64decode(s)
