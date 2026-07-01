from urllib.parse import urlencode

def cache_key(url: str, params: dict) -> str:
    if not params:
        return url
    return f"{url}?{urlencode(sorted(params.items()))}"
