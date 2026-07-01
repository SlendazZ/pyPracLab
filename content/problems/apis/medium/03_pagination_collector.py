# title: Pagination Collector
# track: apis
# difficulty: medium
# tags: api, loop
# description: |
# You have fetch(page) -> {'items': [...], 'total': N} with page size 10. Call fetch for pages 1..N until all items are collected, then return the combined list.
# examples:
# collect(fetch) -> all items across pages
# hint: |
# Loop page=1,2,... ; stop when len(items) >= total.
# syntax_hint: |
# while len(items) < total: page += 1; items.extend(fetch(page)['items'])


def collect(fetch) -> list:
    pass


def run_tests() -> None:
    pages = {1: {'items': ['a', 'b'], 'total': 3}, 2: {'items': ['c'], 'total': 3}}
    def fetch(page):
        return pages[page]
    assert collect(fetch) == ['a', 'b', 'c']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
