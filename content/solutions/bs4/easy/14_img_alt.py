from bs4 import BeautifulSoup

def img_alts(html: str) -> list[str]:
    soup = BeautifulSoup(html, 'html.parser')
    return [img.get('alt', '') for img in soup.find_all('img')]
