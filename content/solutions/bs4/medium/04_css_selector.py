from bs4 import BeautifulSoup

def select_text(html: str, selector: str) -> str:
    tag = BeautifulSoup(html, 'html.parser').select_one(selector)
    return tag.get_text()
