from bs4 import BeautifulSoup

def without_scripts(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all('script'):
        tag.decompose()
    return soup.get_text(strip=True)
