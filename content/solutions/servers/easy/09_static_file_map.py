def mimes(names: list[str]) -> dict[str, str]:
    table = {'html': 'text/html', 'css': 'text/css', 'js': 'application/javascript'}
    out = {}
    for name in names:
        ext = name.rsplit('.', 1)[-1].lower() if '.' in name else ''
        out[name] = table.get(ext, 'application/octet-stream')
    return out
