"""Beautiful Soup problem specs."""

PROBLEMS = [
    {
        "slug": "01_parse_first_tag",
        "track": "bs4", "difficulty": "easy",
        "title": "Parse HTML and Find First Tag",
        "tags": ["bs4", "html"],
        "description": "Parse the HTML string with BeautifulSoup and return the name of the first tag in the document.",
        "examples": "first_tag('<p>hi</p>') -> 'p'",
        "hint": "BeautifulSoup(html, 'html.parser'); soup.find() returns the first element.",
        "syntax_hint": "from bs4 import BeautifulSoup; BeautifulSoup(html, 'html.parser').find().name",
        "signature": "def first_tag(html: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert first_tag('<p>hi</p>') == 'p'\n"
            "    assert first_tag('<div><span>x</span></div>') == 'div'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def first_tag(html: str) -> str:\n"
            "    return BeautifulSoup(html, 'html.parser').find().name\n"
        ),
    },
    {
        "slug": "02_find_by_id",
        "track": "bs4", "difficulty": "easy",
        "title": "Find Element by ID",
        "tags": ["bs4", "html"],
        "description": "Parse the HTML and return the text of the element with the given id attribute.",
        "examples": "text_by_id('<p id=\"main\">hi</p>', 'main') -> 'hi'",
        "hint": "soup.find(id=element_id) or soup.find(attrs={'id': element_id}).",
        "syntax_hint": "BeautifulSoup(html, 'html.parser').find(id='main').get_text()",
        "signature": "def text_by_id(html: str, element_id: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert text_by_id('<p id=\"main\">hi</p>', 'main') == 'hi'\n"
            "    assert text_by_id('<div id=\"x\">one</div><div id=\"y\">two</div>', 'y') == 'two'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def text_by_id(html: str, element_id: str) -> str:\n"
            "    tag = BeautifulSoup(html, 'html.parser').find(id=element_id)\n"
            "    return tag.get_text()\n"
        ),
    },
    {
        "slug": "03_find_by_class",
        "track": "bs4", "difficulty": "easy",
        "title": "Find Elements by Class",
        "tags": ["bs4", "html"],
        "description": "Parse the HTML and return a list of text contents for all elements with the given CSS class.",
        "examples": "texts_by_class('<p class=\"item\">a</p><p class=\"item\">b</p>', 'item') -> ['a', 'b']",
        "hint": "soup.find_all(class_=class_name) returns all matching tags.",
        "syntax_hint": "[t.get_text() for t in soup.find_all(class_='item')]",
        "signature": "def texts_by_class(html: str, class_name: str) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    html = '<p class=\"item\">a</p><p class=\"item\">b</p><p class=\"other\">c</p>'\n"
            "    assert texts_by_class(html, 'item') == ['a', 'b']\n"
            "    assert texts_by_class('<span class=\"x\">z</span>', 'x') == ['z']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def texts_by_class(html: str, class_name: str) -> list[str]:\n"
            "    soup = BeautifulSoup(html, 'html.parser')\n"
            "    return [t.get_text() for t in soup.find_all(class_=class_name)]\n"
        ),
    },
    {
        "slug": "04_css_selector",
        "track": "bs4", "difficulty": "medium",
        "title": "CSS Selector",
        "tags": ["bs4", "css"],
        "description": "Parse the HTML and return the text of the first element matching the CSS selector.",
        "examples": "select_text('<div><p class=\"lead\">hi</p></div>', 'p.lead') -> 'hi'",
        "hint": "soup.select_one(selector) finds the first CSS match.",
        "syntax_hint": "BeautifulSoup(html, 'html.parser').select_one('p.lead').get_text()",
        "signature": "def select_text(html: str, selector: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    html = '<div><p class=\"lead\">hi</p><p class=\"lead\">bye</p></div>'\n"
            "    assert select_text(html, 'p.lead') == 'hi'\n"
            "    assert select_text('<a href=\"#\">link</a>', 'a') == 'link'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def select_text(html: str, selector: str) -> str:\n"
            "    tag = BeautifulSoup(html, 'html.parser').select_one(selector)\n"
            "    return tag.get_text()\n"
        ),
    },
    {
        "slug": "05_link_hrefs",
        "track": "bs4", "difficulty": "medium",
        "title": "Extract Link Hrefs",
        "tags": ["bs4", "html"],
        "description": "Parse the HTML and return a list of href attribute values from all anchor tags, in document order.",
        "examples": "link_hrefs('<a href=\"/a\">A</a><a href=\"/b\">B</a>') -> ['/a', '/b']",
        "hint": "soup.find_all('a') then read tag['href'] for each.",
        "syntax_hint": "[a['href'] for a in soup.find_all('a')]",
        "signature": "def link_hrefs(html: str) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    html = '<a href=\"/a\">A</a><a href=\"/b\">B</a>'\n"
            "    assert link_hrefs(html) == ['/a', '/b']\n"
            "    assert link_hrefs('<p>no links</p>') == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def link_hrefs(html: str) -> list[str]:\n"
            "    soup = BeautifulSoup(html, 'html.parser')\n"
            "    return [a['href'] for a in soup.find_all('a')]\n"
        ),
    },
    {
        "slug": "06_stripped_text",
        "track": "bs4", "difficulty": "medium",
        "title": "Stripped Text Content",
        "tags": ["bs4", "html"],
        "description": "Parse the HTML and return all text from the body with whitespace stripped around each piece, joined by a single space.",
        "examples": "stripped_text('<p>  hello  </p>') -> 'hello'",
        "hint": "get_text(' ', strip=True) joins text chunks with a space.",
        "syntax_hint": "BeautifulSoup(html, 'html.parser').get_text(' ', strip=True)",
        "signature": "def stripped_text(html: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert stripped_text('<p>  hello  </p>') == 'hello'\n"
            "    assert stripped_text('<div><span> a </span><span> b </span></div>') == 'a b'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def stripped_text(html: str) -> str:\n"
            "    return BeautifulSoup(html, 'html.parser').get_text(' ', strip=True)\n"
        ),
    },
    {
        "slug": "07_table_to_dicts",
        "track": "bs4", "difficulty": "medium",
        "title": "HTML Table to Dicts",
        "tags": ["bs4", "html"],
        "description": "Parse an HTML table with a header row and data rows. Return a list of dicts mapping header text to cell text for each data row.",
        "examples": "table_rows('<table><tr><th>Name</th><th>Age</th></tr><tr><td>Ada</td><td>36</td></tr></table>') -> [{'Name': 'Ada', 'Age': '36'}]",
        "hint": "Read th texts as keys; for each tr in tbody (or after header), zip headers with td texts.",
        "syntax_hint": "headers = [th.get_text(strip=True) for th in row.find_all('th')]",
        "signature": "def table_rows(html: str) -> list[dict[str, str]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    html = (\n"
            "        '<table><tr><th>Name</th><th>Age</th></tr>'\n"
            "        '<tr><td>Ada</td><td>36</td></tr>'\n"
            "        '<tr><td>Bob</td><td>40</td></tr></table>'\n"
            "    )\n"
            "    assert table_rows(html) == [\n"
            "        {'Name': 'Ada', 'Age': '36'},\n"
            "        {'Name': 'Bob', 'Age': '40'},\n"
            "    ]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def table_rows(html: str) -> list[dict[str, str]]:\n"
            "    soup = BeautifulSoup(html, 'html.parser')\n"
            "    table = soup.find('table')\n"
            "    rows = table.find_all('tr')\n"
            "    headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]\n"
            "    result = []\n"
            "    for row in rows[1:]:\n"
            "        cells = [td.get_text(strip=True) for td in row.find_all('td')]\n"
            "        result.append(dict(zip(headers, cells)))\n"
            "    return result\n"
        ),
    },
    {
        "slug": "08_visible_text",
        "track": "bs4", "difficulty": "hard",
        "title": "Visible Text Without Scripts",
        "tags": ["bs4", "html"],
        "description": "Parse the HTML, remove script and style elements, then return the remaining visible text with whitespace stripped.",
        "examples": "visible_text('<p>hi</p><script>alert(1)</script>') -> 'hi'",
        "hint": "soup.find_all(['script', 'style']) then decompose() each before get_text.",
        "syntax_hint": "for tag in soup.find_all(['script', 'style']): tag.decompose()",
        "signature": "def visible_text(html: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    html = '<html><head><style>body{}</style></head><body><p>hi</p><script>x=1</script></body></html>'\n"
            "    assert visible_text(html) == 'hi'\n"
            "    assert visible_text('<style>.x{}</style><div> ok </div>') == 'ok'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from bs4 import BeautifulSoup\n\n"
            "def visible_text(html: str) -> str:\n"
            "    soup = BeautifulSoup(html, 'html.parser')\n"
            "    for tag in soup.find_all(['script', 'style']):\n"
            "        tag.decompose()\n"
            "    return soup.get_text(strip=True)\n"
        ),
    },
]
