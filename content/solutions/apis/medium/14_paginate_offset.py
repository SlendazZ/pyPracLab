import math

def page_items(items: list, page: int, size: int) -> tuple[list, int]:
    if not items or size <= 0:
        return [], 0
    total = math.ceil(len(items) / size)
    start = (page - 1) * size
    return items[start:start + size], total
