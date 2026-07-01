# title: Simple LRU Cache
# track: apps
# difficulty: hard
# tags: class, cache
# description: |
# LRUCache(capacity) with get(key) and put(key, val); evict least recently used when full.
# examples:
# c=LRUCache(2); c.put(1,1); c.put(2,2); c.put(3,3); c.get(1) is None
# hint: |
# OrderedDict move_to_end on access; popitem(last=False) to evict.
# syntax_hint: |
# from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int): pass
    def get(self, key): pass
    def put(self, key, value) -> None: pass


def run_tests() -> None:
    c = LRUCache(2)
    c.put(1, 'a')
    c.put(2, 'b')
    assert c.get(1) == 'a'
    c.put(3, 'c')
    assert c.get(2) is None
    assert c.get(3) == 'c'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
