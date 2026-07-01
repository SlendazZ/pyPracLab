# title: Merge Paginated Items
# track: apis
# difficulty: easy
# tags: list
# description: |
# Given a list of page dicts each with an 'items' list, return one combined list of all items.
# examples:
# merge_pages([{'items':[1]},{'items':[2,3]}]) -> [1,2,3]
# hint: |
# A nested comprehension or itertools.chain flattens them.
# syntax_hint: |
# [item for page in pages for item in page['items']]


def merge_pages(pages: list[dict]) -> list:
    pass


def run_tests() -> None:
    assert merge_pages([{'items': [1]}, {'items': [2, 3]}]) == [1, 2, 3]
    assert merge_pages([]) == []
    assert merge_pages([{'items': []}]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
