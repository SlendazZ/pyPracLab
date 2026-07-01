from urllib.parse import urljoin

def join_url(base: str, *parts: str) -> str:
    url = base
    for part in parts:
        if not part:
            continue
        url = urljoin(url.rstrip('/') + '/', part.lstrip('/'))
    return url
