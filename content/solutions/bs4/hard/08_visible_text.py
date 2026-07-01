from bs4 import BeautifulSoup

def visible_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(['script', 'style']):
        tag.decompose()
    return soup.get_text(strip=True)
