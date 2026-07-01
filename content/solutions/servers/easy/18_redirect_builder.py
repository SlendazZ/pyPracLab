def redirect(url: str, status: int = 302) -> dict:
    return {'status': status, 'headers': {'Location': url}, 'body': ''}
