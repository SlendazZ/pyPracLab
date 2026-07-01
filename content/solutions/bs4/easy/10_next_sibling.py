from bs4 import BeautifulSoup

def next_after_h1(html: str) -> str | None:
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.find('h1')
    if h1 is None:
        return None
    sib = h1.find_next_sibling()
    if sib is None:
        return None
    return sib.get_text(strip=True)
