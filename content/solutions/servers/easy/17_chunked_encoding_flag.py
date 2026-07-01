def is_chunked(headers: dict[str, str]) -> bool:
    for k, v in headers.items():
        if k.lower() == 'transfer-encoding':
            return 'chunked' in v.lower()
    return False
