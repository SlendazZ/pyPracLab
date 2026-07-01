from urllib.parse import urlencode

def encode_params(params: dict) -> str:
    return urlencode(params)
