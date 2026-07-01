---
title: Regular Expressions in Python
track: automations
difficulty: easy
tags: regex, re
exercise: content/problems/automations/easy/02_extract_emails.py
---

# Regular Expressions in Python

## Overview

The `re` module matches patterns in text. Automations use regex for log parsing, validation, extraction, and cleanup — but prefer simpler tools (split, str methods) when they suffice.

A regular expression is a tiny language for describing text shapes: digits, word characters, optional parts, repeated sections. You do not need to memorize every feature on day one — start with `search`, `findall`, and named groups, then grow from there.

Rule of thumb: if `text.startswith`, `in`, or `split` solves the problem, skip regex. Reach for it when the structure varies (emails, IPs, log fields).

## Your first pattern

Suppose you want the first number in a string:

```python
import re

text = 'Order 42 shipped to ada@example.com'
match = re.search(r'\d+', text)
if match:
    print(match.group())   # '42'
    print(match.start())   # 6 — index where match begins
```

Read `r'\d+'` as: one or more digits. The `r` prefix is a raw string — backslashes are passed to the regex engine without Python eating them first.

## Core functions

Four functions cover most automation tasks:

```python
import re

text = 'Order 42 shipped to ada@example.com'

re.search(r'\d+', text)            # first match or None
re.findall(r'\w+@\w+', text)       # all matches as strings
re.sub(r'\s+', ' ', text)          # replace every match
re.split(r'[,;]', 'a,b;c')           # split on pattern
```

Use raw strings `r'...'` so backslashes behave as regex expects. In `r'\d+'`, Python passes `\d+` to the regex engine (digit, one or more).

Three ways to anchor a match:

```python
re.match(r'\d+', text)      # only at the start of the string
re.search(r'\d+', text)     # anywhere in the string
re.fullmatch(r'\d+', '42')  # entire string must match
```

`match` is often the wrong choice — most beginners want `search` or `fullmatch`. Use `fullmatch` when validating a whole line (a zip code, an ID).

## Groups and capture

Parentheses capture parts of a match. Named groups make extraction readable:

```python
email = 'ada.lovelace@example.co.uk'
m = re.search(r'(?P<user>[\w.+-]+)@(?P<domain>[\w.-]+)', email)
if m:
    print(m.group('user'))    # 'ada.lovelace'
    print(m.group('domain'))  # 'example.co.uk'
    print(m.group(0))         # full match
```

Always check `if m:` before calling `group()` — otherwise you get `AttributeError: 'NoneType' object has no attribute 'group'`.

Extract area code and local number from a phone string:

```python
PHONE = re.compile(r'\((?P<area>\d{3})\) (?P<local>\d{3}-\d{4})')
m = PHONE.search('Call (555) 123-4567 today')
if m:
    print(m['area'], m['local'])   # same as group('area')
```

## Common pattern building blocks

| Token | Meaning        | Example match   |
|-------|----------------|-----------------|
| `.`   | any char       | `a`, `9`, space |
| `\d`  | digit          | `0`–`9`         |
| `\w`  | word char      | `a`, `_`, `9`   |
| `\s`  | whitespace     | space, tab      |
| `+`   | one or more    | `\d+` → `42`   |
| `*`   | zero or more   | `\d*` → `` or `7` |
| `?`   | optional       | `-?\d` → `5` or `-5` |
| `^` `$`| start / end   | `^OK$` whole line |
| `[]`  | char class     | `[aeiou]` vowel |

Square brackets list allowed characters. `[^\d]` means not a digit.

Practice reading patterns aloud:

```python
r'^ERROR \d{4}-\d{2}-\d{2}'   # line starts with ERROR and a date
r'\bpython\b'                  # whole word python, not xpythony
r'file_\d{3}\.txt'             # file_001.txt, file_042.txt
```

## Worked example: extract emails from a blob

Start simple, then tighten the pattern as you see edge cases:

```python
import re

blob = '''
Contact ada@example.com or support@my-company.io.
Invalid: not-an-email@
Also: bob.smith+tag@mail.org
'''

EMAIL = re.compile(r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}')
found = EMAIL.findall(blob)
print(found)
# ['ada@example.com', 'support@my-company.io', 'bob.smith+tag@mail.org']
```

Step by step:
1. `re.compile` builds the pattern once — reuse it when scanning many lines.
2. `[\w.+-]+` allows letters, digits, dots, plus, hyphen in the local part.
3. `[a-zA-Z]{2,}` requires a TLD of at least two letters.
4. `findall` returns plain strings; use `finditer` if you need match objects.

Deduplicate while preserving order:

```python
def unique_emails(text: str) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for addr in EMAIL.findall(text):
        key = addr.lower()
        if key not in seen:
            seen.add(key)
            result.append(addr)
    return result
```

## Worked example: parse a log line

Logs often follow a fixed template with variable fields:

```python
import re

LINE = re.compile(
    r'^(?P<level>\w+) (?P<ts>\d{4}-\d{2}-\d{2}) '
    r'(?P<msg>.+)$'
)
line = 'ERROR 2026-06-30 Disk full on /var'
m = LINE.search(line)
if m:
    record = m.groupdict()
    if record['level'] == 'ERROR':
        print(record['msg'])
```

`groupdict()` returns `{'level': 'ERROR', 'ts': '2026-06-30', ...}` — handy for feeding into CSV or JSON output.

Process a whole log file:

```python
from pathlib import Path

def error_messages(path: Path) -> list[str]:
    errors = []
    for line in path.read_text(encoding='utf-8').splitlines():
        m = LINE.search(line)
        if m and m['level'] == 'ERROR':
            errors.append(m['msg'])
    return errors
```

## Worked example: clean messy whitespace

Regex shines at repetitive cleanup:

```python
import re

messy = '  hello\t\tworld  \n\n  foo  '
cleaned = re.sub(r'\s+', ' ', messy).strip()
print(cleaned)   # 'hello world foo'
```

Remove HTML tags (simple cases only):

```python
html = '<p>Hi <b>there</b></p>'
plain = re.sub(r'<[^>]+>', '', html)
print(plain)   # 'Hi there'
```

## Compiling for reuse

When the same pattern runs hundreds of times, compile it once:

```python
EMAIL = re.compile(r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}')
for line in path.read_text().splitlines():
    for addr in EMAIL.findall(line):
        print(addr)
```

Flags modify behavior. Common ones:

```python
re.compile(r'^start', re.MULTILINE)   # ^ matches each line
re.compile(r'foo', re.IGNORECASE)     # case-insensitive
re.compile(r'#.*$', re.MULTILINE)     # strip end-of-line comments
```

## Common pitfalls

- Over-using regex for fixed-string replace (`str.replace`)
- Catastrophic backtracking on nested quantifiers — keep patterns simple
- Forgetting `re.MULTILINE` when `^`/`$` must match line boundaries
- Greedy `.*` swallowing too much — use non-greedy `.*?` or explicit groups
- Validating emails with one giant regex — extract first, validate later
- Testing only happy paths — feed real messy data from production logs

## Practice

Extract email addresses from a block of text.

## Summary

Regex excels at semi-structured text. Test patterns on real samples; compile once when scanning many lines. Start with `search` and `findall`, use named groups for clarity, and prefer simpler string tools when they fit.
