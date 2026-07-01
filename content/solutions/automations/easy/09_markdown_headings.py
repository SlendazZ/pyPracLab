import re

def headings(text: str) -> list[str]:
    return re.findall(r'^#+\s+(.+)$', text, re.MULTILINE)
