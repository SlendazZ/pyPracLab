from bs4 import BeautifulSoup

def parent_name(html: str) -> str | None:
    soup = BeautifulSoup(html, 'html.parser')
    span = soup.find('span')
    if span is None or span.parent is None:
        return None
    return span.parent.name
