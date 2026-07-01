def parse_host(value: str) -> tuple[str, int]:
    host, _, port = value.partition(':')
    return host, int(port) if port else 80
