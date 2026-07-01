# title: Offset Pagination
# track: apis
# difficulty: medium
# tags: api
# description: |
# Slice items for page (1-based) and page_size; return (items_slice, total_pages).
# examples:
# page_items([1,2,3,4,5], page=2, size=2) -> ([3,4], 3)
# hint: |
# start = (page-1)*size; math.ceil for total pages.
# syntax_hint: |
# import math; math.ceil(len(items)/size)


def page_items(items: list, page: int, size: int) -> tuple[list, int]:
    pass


def run_tests() -> None:
    assert page_items([1,2,3,4,5], 2, 2) == ([3,4], 3)
    assert page_items([], 1, 10) == ([], 0)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
