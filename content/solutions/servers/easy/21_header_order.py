def order_headers(headers: dict[str, str]) -> list[tuple[str, str]]:
    return sorted(headers.items(), key=lambda kv: kv[0].lower())
