from bs4 import BeautifulSoup

def first_tag(html: str) -> str:
    return BeautifulSoup(html, 'html.parser').find().name
