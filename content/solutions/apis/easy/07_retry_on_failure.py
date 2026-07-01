def retry(fn, n: int):
    last = None
    for _ in range(n):
        try:
            return fn()
        except Exception as e:
            last = e
    raise last
