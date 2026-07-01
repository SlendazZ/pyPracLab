from bs4 import BeautifulSoup

def texts_by_class(html: str, class_name: str) -> list[str]:
    soup = BeautifulSoup(html, 'html.parser')
    return [t.get_text() for t in soup.find_all(class_=class_name)]
