from contextlib import suppress

def safe_get(d: dict, key: str, default):
    with suppress(KeyError):
        return d[key]
    return default
