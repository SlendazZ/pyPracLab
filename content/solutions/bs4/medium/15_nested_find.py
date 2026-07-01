from bs4 import BeautifulSoup

def main_link(html: str) -> str | None:
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='main')
    if div is None:
        return None
    a = div.find('a')
    if a is None:
        return None
    return a.get('href')
