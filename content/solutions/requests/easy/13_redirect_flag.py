def should_follow(allow: bool, status: int) -> bool:
    if status in (301, 302, 303, 307, 308):
        return allow
    return True
