def parse(argv: list[str]) -> dict:
    out = {}
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg.startswith('--'):
            key = arg[2:]
            if i + 1 < len(argv) and not argv[i + 1].startswith('--'):
                out[key] = argv[i + 1]
                i += 1
            else:
                out[key] = True
        i += 1
    return out
