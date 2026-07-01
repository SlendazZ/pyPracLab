from bs4 import BeautifulSoup

def paragraph_texts(html: str) -> list[str]:
    soup = BeautifulSoup(html, 'html.parser')
    return [p.get_text(strip=True) for p in soup.find_all('p')]
