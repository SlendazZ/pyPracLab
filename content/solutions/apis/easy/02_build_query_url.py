from urllib.parse import urlencode

def build_url(base: str, params: dict) -> str:
    cleaned = {k: v for k, v in params.items() if v is not None}
    if not cleaned:
        return base
    return f"{base}?{urlencode(cleaned)}"
