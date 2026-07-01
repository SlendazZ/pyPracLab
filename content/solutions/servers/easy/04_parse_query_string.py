import urllib.parse

def parse_qs(q: str) -> dict[str, str]:
    return {k: v[0] for k, v in urllib.parse.parse_qs(q).items()}
