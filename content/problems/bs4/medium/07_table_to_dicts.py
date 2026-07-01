# title: HTML Table to Dicts
# track: bs4
# difficulty: medium
# tags: bs4, html
# description: |
# Parse an HTML table with a header row and data rows. Return a list of dicts mapping header text to cell text for each data row.
# examples:
# table_rows('<table><tr><th>Name</th><th>Age</th></tr><tr><td>Ada</td><td>36</td></tr></table>') -> [{'Name': 'Ada', 'Age': '36'}]
# hint: |
# Read th texts as keys; for each tr in tbody (or after header), zip headers with td texts.
# syntax_hint: |
# headers = [th.get_text(strip=True) for th in row.find_all('th')]


def table_rows(html: str) -> list[dict[str, str]]:
    pass


def run_tests() -> None:
    html = (
        '<table><tr><th>Name</th><th>Age</th></tr>'
        '<tr><td>Ada</td><td>36</td></tr>'
        '<tr><td>Bob</td><td>40</td></tr></table>'
    )
    assert table_rows(html) == [
        {'Name': 'Ada', 'Age': '36'},
        {'Name': 'Bob', 'Age': '40'},
    ]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
