def escape_markup(s: str) -> str:
    return s.replace('[', '\\[').replace(']', '\\]')
