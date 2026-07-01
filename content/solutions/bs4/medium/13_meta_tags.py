from bs4 import BeautifulSoup

def meta_dict(html: str) -> dict[str, str]:
    soup = BeautifulSoup(html, 'html.parser')
    out: dict[str, str] = {}
    for m in soup.find_all('meta'):
        name = m.get('name')
        if name:
            out[name] = m.get('content', '')
    return out
