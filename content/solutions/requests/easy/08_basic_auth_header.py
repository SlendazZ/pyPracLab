import base64

def auth_header(user: str, password: str) -> str:
    token = base64.b64encode(f'{user}:{password}'.encode()).decode()
    return f'Basic {token}'
