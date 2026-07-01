def status_class(code: int) -> str:
    classes = {2: 'success', 3: 'redirect', 4: 'client', 5: 'server'}
    return classes.get(code // 100, 'unknown')
