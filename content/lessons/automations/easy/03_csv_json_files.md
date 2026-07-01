---
title: CSV, JSON, and Line-Oriented Files
track: automations
difficulty: easy
tags: csv, json, files
exercise: content/problems/automations/easy/13_json_lines_parse.py
---

# CSV, JSON, and Line-Oriented Files

## Overview

Most automation scripts ingest or emit structured text: CSV spreadsheets, JSON configs, JSON Lines logs. Python's stdlib handles all three without extra dependencies.

Choosing a format is usually not your decision — the data arrives as CSV from a spreadsheet export, JSON from an API, or JSONL from a log pipeline. Your job is to parse it safely, transform it, and write it back without corrupting structure (embedded commas, unicode, nested fields).

This lesson walks through each format with small examples, then combines them in a realistic pipeline.

## JSON: Python values ↔ text

JSON maps closely to Python: objects → dict, arrays → list, strings, numbers, booleans, and `null` → `None`.

```python
import json

data = {'name': 'Ada', 'scores': [98, 87], 'active': True}
text = json.dumps(data, indent=2)   # Python → string
back = json.loads(text)             # string → Python
```

Read and write files with `load` / `dump` (note the `f`):

```python
from pathlib import Path

config_path = Path('config.json')
with config_path.open(encoding='utf-8') as f:
    config = json.load(f)

config['debug'] = True
with config_path.open('w', encoding='utf-8') as f:
    json.dump(config, f, indent=2)
```

JSON requires double quotes; keys in objects must be strings. Trailing commas and comments are not valid JSON.

Beginner tip: `loads`/`dumps` work on strings; `load`/`dump` work on file objects. The extra `s` means string.

Pretty-print for humans, compact for APIs:

```python
json.dumps(data)                          # compact one-liner
json.dumps(data, indent=2)                # readable config file
json.dumps(data, ensure_ascii=False)      # keep é, ñ, 中文 as-is
```

## JSON Lines (JSONL)

One JSON object per line — common for logs and ML datasets. Each line is independent, so you can stream huge files without loading everything:

```python
import json
from pathlib import Path

def load_jsonl(path: Path) -> list[dict]:
    records = []
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line:
            records.append(json.loads(line))
    return records
```

Write JSONL the same way — one `dumps` call per line:

```python
def save_jsonl(path: Path, records: list[dict]) -> None:
    lines = [json.dumps(r, ensure_ascii=False) for r in records]
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
```

Stream a large file without building a giant list:

```python
def iter_jsonl(path: Path):
    with path.open(encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)

for event in iter_jsonl(Path('events.jsonl')):
    if event.get('level') == 'ERROR':
        print(event['message'])
```

## CSV: tabular data

CSV files look like spreadsheets: a header row, then data rows. Use the `csv` module — never split on commas by hand (fields can contain commas inside quotes).

Why not `line.split(',')`? This row breaks naive splitting:

```
Ada,"123 Main St, Apt 4",120
```

The address field contains a comma inside quotes. `csv` handles that.

Reading rows as dictionaries (column name → value):

```python
import csv
from pathlib import Path

with Path('data.csv').open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['amount'])
```

Writing a CSV from scratch:

```python
rows = [
    {'name': 'Ada', 'amount': '120'},
    {'name': 'Grace', 'amount': '95'},
]
with Path('out.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'amount'])
    writer.writeheader()
    writer.writerows(rows)
```

Always open CSV with `newline=''` to avoid extra blank lines on Windows.

Convert string columns to numbers after reading:

```python
def load_sales(path: Path) -> list[dict]:
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [
            {**row, 'amount': int(row['amount'])}
            for row in reader
        ]
```

`DictReader` returns every value as a string — convert numbers yourself.

## Worked example: JSONL log → summary CSV

Combine formats in a typical pipeline — read events, aggregate, export:

```python
import csv
import json
from collections import Counter
from pathlib import Path

def summarize_events(jsonl_path: Path, csv_path: Path) -> None:
    counts: Counter[str] = Counter()
    for line in jsonl_path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        counts[event['type']] += 1

    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['type', 'count'])
        for event_type, count in counts.most_common():
            writer.writerow([event_type, count])
```

Step by step:
1. Stream the JSONL file line by line (memory-safe).
2. `json.loads` each non-empty line into a dict.
3. Tally with `Counter`.
4. Write a simple two-column CSV with `csv.writer`.

Sample input (`events.jsonl`):

```json
{"type": "click", "user": "ada"}
{"type": "view", "user": "bob"}
{"type": "click", "user": "ada"}
```

Output (`summary.csv`):

```
type,count
click,2
view,1
```

## Worked example: merge JSON config with CSV defaults

Sometimes automation reads a JSON config and a CSV lookup table:

```python
import csv
import json
from pathlib import Path

def load_role_map(csv_path: Path) -> dict[str, str]:
    with csv_path.open(newline='', encoding='utf-8') as f:
        return {row['email']: row['role'] for row in csv.DictReader(f)}

config = json.loads(Path('config.json').read_text(encoding='utf-8'))
roles = load_role_map(Path('roles.csv'))
admin_emails = [e for e, r in roles.items() if r == 'admin']
config['notify'] = admin_emails
Path('config.json').write_text(
    json.dumps(config, indent=2), encoding='utf-8'
)
```

## When to use which

| Format | Good for                    | Avoid when…              |
|--------|-----------------------------|--------------------------|
| CSV    | tabular exports, spreadsheets| deeply nested data      |
| JSON   | nested configs, APIs        | multi-GB single blob     |
| JSONL  | streaming logs, big datasets| you need one array file  |

## Common pitfalls

- `json.loads` on empty string raises — guard with `strip()`
- CSV with embedded commas needs proper quoting (use csv module)
- Loading multi-GB JSON into memory — stream JSONL line by line
- `json.dump` without `ensure_ascii=False` escapes non-ASCII as `\uXXXX`
- DictReader returns every value as a string — convert numbers yourself
- Forgetting `newline=''` on CSV — extra blank lines on Windows
- Assuming JSON from the web is valid — wrap `loads` in try/except

## Practice

Parse JSON Lines into a list of dicts.

## Summary

Pick the format your data already uses; use stdlib readers instead of manual splitting when structure matters. JSON for nested configs, CSV for tables, JSONL for streams — and always set `encoding='utf-8'` plus `newline=''` for CSV.
