def collect(fetch) -> list:
    items: list = []
    total = None
    page = 0
    while total is None or len(items) < total:
        page += 1
        data = fetch(page)
        items.extend(data['items'])
        total = data['total']
    return items
