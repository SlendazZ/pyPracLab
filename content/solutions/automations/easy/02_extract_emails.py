import re

def extract_emails(text: str) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for m in re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text):
        if m not in seen:
            seen.add(m)
            result.append(m)
    return result
