import re

def route(routes: list[tuple[str, str]], path: str) -> tuple:
    for pattern, handler in routes:
        regex = '^' + re.sub(r'<(\w+)>', r'(?P<\1>[^/]+)', pattern) + '$'
        m = re.match(regex, path)
        if m:
            return handler, m.groupdict()
    return None, {}
