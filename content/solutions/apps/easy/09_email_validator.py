import re

def is_email(s: str) -> bool:
    return re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', s) is not None
