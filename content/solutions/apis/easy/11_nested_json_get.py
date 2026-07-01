import json

def user_name(text: str) -> str | None:
    obj = json.loads(text)
    return obj.get('user', {}).get('name')
