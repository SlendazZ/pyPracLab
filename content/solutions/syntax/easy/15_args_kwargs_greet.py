def greet(greeting: str, *names, **punctuation) -> str:
    punct = punctuation.get('punct', '')
    return f"{greeting}, {' and '.join(names)}{punct}"
