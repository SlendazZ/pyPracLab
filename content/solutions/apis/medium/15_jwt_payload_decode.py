import base64
import json

def decode_payload(token: str) -> dict:
    payload = token.split('.')[1]
    padded = payload + '=' * (-len(payload) % 4)
    return json.loads(base64.urlsafe_b64decode(padded))
