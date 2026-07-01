import json

def key_count(text: str) -> int:
    return len(json.loads(text))
