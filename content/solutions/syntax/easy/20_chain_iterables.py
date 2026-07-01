from itertools import chain

def flatten(items: list[list]) -> list:
    return list(chain.from_iterable(items))
