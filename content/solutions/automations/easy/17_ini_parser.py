def parse_section(text: str, section: str) -> dict[str, str]:
    result: dict[str, str] = {}
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('[') and line.endswith(']'):
            current = line[1:-1]
            continue
        if current == section and '=' in line:
            k, v = line.split('=', 1)
            result[k.strip()] = v.strip()
    return result
