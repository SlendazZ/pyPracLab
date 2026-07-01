def merge_pages(pages: list[dict]) -> list:
    return [item for page in pages for item in page['items']]
