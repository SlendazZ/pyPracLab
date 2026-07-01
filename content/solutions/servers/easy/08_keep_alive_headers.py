def parse_headers(text: str) -> dict[str, str]:
    out = {}
    for line in text.splitlines():
        if ': ' in line:
            k, v = line.split(': ', 1)
            out[k.lower()] = v
    return out
