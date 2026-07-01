from bs4 import BeautifulSoup

def link_hrefs(html: str) -> list[str]:
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.find_all('a')]
