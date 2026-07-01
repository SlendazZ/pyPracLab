from bs4 import BeautifulSoup

def text_by_id(html: str, element_id: str) -> str:
    tag = BeautifulSoup(html, 'html.parser').find(id=element_id)
    return tag.get_text()
