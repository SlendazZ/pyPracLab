def error_label(code: int) -> str:
    cls = code // 100
    if cls == 2:
        return 'ok'
    if cls == 4:
        return 'client'
    if cls == 5:
        return 'server'
    return 'unknown'
