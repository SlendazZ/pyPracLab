import json

def get_data(text: str):
    return json.loads(text)['data']
