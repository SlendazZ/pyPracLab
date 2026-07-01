---
title: Beautiful Soup Basics
track: bs4
difficulty: easy
tags: bs4, html
exercise: content/problems/bs4/easy/01_parse_first_tag.py
---

# Beautiful Soup Basics

## Overview

Beautiful Soup turns HTML and XML into a tree of Python objects you can search, traverse, and modify. It is the go-to library when you need to extract data from web pages, email templates, or exported reports.

You do not need to understand the full HTML spec. Beautiful Soup repairs common markup mistakes and gives you Python methods to find the pieces you care about.

Real-world uses:

- Scraping product prices from an e-commerce page
- Parsing HTML email digests for headlines and links
- Extracting table rows from a saved financial report
- Cleaning messy markup before feeding it to another tool

Install with `pip install beautifulsoup4`. You also need a parser:

| Parser        | Install          | Speed   | Notes                    |
|---------------|------------------|---------|--------------------------|
| `html.parser` | built-in         | moderate| good default, no extras  |
| `lxml`        | `pip install lxml` | fast  | best for large documents |
| `html5lib`    | `pip install html5lib` | slow | most lenient parsing |

## Parse a document

```python
from bs4 import BeautifulSoup

html = '<p class="lead">Hello</p>'
soup = BeautifulSoup(html, 'html.parser')
tag = soup.find('p')
print(tag.name)        # p
print(tag.get_text())  # Hello
print(tag['class'])    # ['lead']
```

The **first tag** in the document is available as `soup.contents[0]` (skipping the root `[document]` node) or via `find()`. The exercise asks you to identify that first tag's name.

```python
first = soup.find()          # first tag in the tree
first.name                   # e.g. 'p', 'html', 'div'
```

## The parse tree mental model

Think of HTML as nested boxes:

```
html
 └── body
      ├── h1  ("Products")
      └── ul
           ├── li → a ("Shoes")
           └── li → a ("Hats")
```

Every element is a `Tag`. Text between tags is a `NavigableString`. You navigate with `.parent`, `.children`, `.next_sibling`, and search methods like `.find()` and `.find_all()`.

```python
link = soup.find('a')
link.name           # 'a'
link.string         # direct text child, or None
link.parent.name    # 'li'
link['href']        # attribute value
```

## Finding elements

### By tag name

```python
soup.find('title')            # first <title>, or None
soup.find_all('a')            # list of every <a>
soup.find_all('li', limit=5)  # stop after 5 matches
soup.find_all(['h1', 'h2'])   # all h1 and h2 tags
```

`find` returns **one** tag or `None`. `find_all` always returns a **list** (possibly empty).

### By attribute

HTML `class` is a reserved word in Python, so use `class_`:

```python
soup.find(id='main-content')
soup.find_all(class_='product-card')
soup.find('input', attrs={'name': 'email', 'type': 'text'})
soup.find('div', {'data-id': '42'})   # shorthand for attrs
```

The `class` attribute is often a **list** of class names:

```python
tag = soup.find(class_='btn')
tag['class']   # ['btn', 'primary', 'large']
'primary' in tag.get('class', [])   # safe membership check
```

### CSS selectors

If you know CSS, `select` is often the clearest option:

```python
soup.select_one('p.lead')               # first <p class="lead">
soup.select('ul.menu li a')             # all links inside menu lists
soup.select('div.product span.price')   # prices inside product divs
soup.select('[data-sku]')               # any element with data-sku attr
```

## Worked example: scrape a product list

```python
html = '''
<ul class="products">
  <li data-sku="A1"><span class="name">Widget</span><span class="price">$9.99</span></li>
  <li data-sku="B2"><span class="name">Gadget</span><span class="price">$14.50</span></li>
</ul>
'''
soup = BeautifulSoup(html, 'html.parser')
products = []
for item in soup.select('ul.products li'):
    products.append({
        'sku': item['data-sku'],
        'name': item.select_one('.name').get_text(strip=True),
        'price': item.select_one('.price').get_text(strip=True),
    })
# [{'sku': 'A1', 'name': 'Widget', 'price': '$9.99'},
#  {'sku': 'B2', 'name': 'Gadget', 'price': '$14.50'}]
```

This pattern — loop containers, extract fields with `select_one` — covers most scraping tasks.

## Worked example: HTML table to list of dicts

Reports and dashboards often use `<table>`:

```python
html = '''
<table>
  <tr><th>Name</th><th>Score</th></tr>
  <tr><td>Ada</td><td>98</td></tr>
  <tr><td>Grace</td><td>95</td></tr>
</table>
'''
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find('table').find_all('tr')
headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
records = []
for row in rows[1:]:
    cells = [td.get_text(strip=True) for td in row.find_all('td')]
    records.append(dict(zip(headers, cells)))
# [{'Name': 'Ada', 'Score': '98'}, {'Name': 'Grace', 'Score': '95'}]
```

## Text extraction

```python
tag.get_text()               # all text, including children
tag.get_text(strip=True)     # trim whitespace on each piece
tag.get_text(separator=' ')  # join fragments with a space
tag.get_text(separator='\n', strip=True)  # one line per block
```

**Cleaning invisible junk:** scripts and styles hold text you usually do not want. Remove them before extracting visible text:

```python
for bad in soup(['script', 'style', 'noscript']):
    bad.decompose()  # remove from tree entirely
visible = soup.get_text(separator='\n', strip=True)
```

## Traversing the tree

```python
link = soup.find('a')
link['href']              # attribute value
link.parent.name          # enclosing tag name
link.next_sibling         # node after this tag (may be whitespace)
link.find_next('span')    # next <span> anywhere after this tag
list(link.children)       # direct child nodes
link.descendants          # all nested nodes (generator)
```

Whitespace between tags becomes `NavigableString` nodes — use `.strip()` or `get_text(strip=True)` to ignore them.

## Worked example: extract all links

```python
page = '''
<html><body>
  <a href="/home">Home</a>
  <a href="https://example.com/docs">Docs</a>
  <a href="/about">About</a>
</body></html>
'''
soup = BeautifulSoup(page, 'html.parser')
links = [
    {'text': a.get_text(strip=True), 'href': a['href']}
    for a in soup.find_all('a', href=True)
]
# [{'text': 'Home', 'href': '/home'}, ...]
```

Use `href=True` to skip anchor tags without an href attribute.

## Real-world scenario: price change monitor

```python
import httpx
from bs4 import BeautifulSoup

def fetch_price(url: str, selector: str) -> str:
    r = httpx.get(url, timeout=10, follow_redirects=True)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    el = soup.select_one(selector)
    if el is None:
        raise ValueError(f'selector not found: {selector}')
    return el.get_text(strip=True)

# price = fetch_price('https://shop.example/item/42', 'span.price')
```

Always respect `robots.txt`, terms of service, and rate limits when scraping live sites. Cache responses during development.

## Parsing from a file or HTTP response

```python
from pathlib import Path
html = Path('report.html').read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
```

With httpx:

```python
import httpx
from bs4 import BeautifulSoup

r = httpx.get('https://example.com', timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')
```

Always specify encoding when reading files (`utf-8` is typical).

## Defensive scraping

Websites change layout. Write selectors that fail loudly:

```python
def safe_text(soup, selector: str, default: str = '') -> str:
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else default

name = safe_text(soup, 'span.product-name')
if not name:
    print('warning: product name missing — page layout may have changed')
```

## Modifying the tree

Beautiful Soup can also build or fix HTML:

```python
new_tag = soup.new_tag('b')
new_tag.string = 'important'
soup.find('p').append(new_tag)
print(soup.prettify())
```

Useful when generating email HTML or normalizing broken markup.

## find vs find_all vs select

| Method       | Returns              | Best for                    |
|--------------|----------------------|-----------------------------|
| `find`       | first match or None  | single element              |
| `find_all`   | list (maybe empty)   | all matches, filter by attr |
| `select`     | list via CSS         | complex nested selectors    |
| `select_one` | first CSS match      | one element by CSS          |

## Common pitfalls

- Using `class=` instead of `class_=` (syntax error)
- Expecting `find` to return a list (it returns one tag or `None`)
- Forgetting that blank lines between tags are text nodes
- Treating `class` as a string when it can be a list
- Assuming HTML structure never changes — write defensive selectors
- Not specifying encoding when reading files
- Calling `.get_text()` on `None` because `find` returned nothing

## Practice

Parse HTML and return the name of the first tag.

## Summary

Beautiful Soup turns markup into a searchable tree. Parse with `BeautifulSoup(html, 'html.parser')`, locate elements with `find`, `find_all`, or `select`, and extract data with `.get_text(strip=True)` and attribute access. Loop container elements and pull fields — that pattern scales to real scraping jobs.
