# title: Parse INI Section
# track: automations
# difficulty: easy
# tags: config
# description: |
# Parse simple INI text with one [section] and key=value lines into dict for that section.
# examples:
# [app]\nname=demo -> {'name':'demo'}
# hint: |
# Split lines; on [section] start; key=value split once.
# syntax_hint: |
# line.strip(); if line.startswith('['): ...


def parse_section(text: str, section: str) -> dict[str, str]:
    pass


def run_tests() -> None:
    t = '[app]\nname=demo\nport=80\n[db]\nhost=localhost'
    assert parse_section(t, 'app') == {'name': 'demo', 'port': '80'}
    assert parse_section(t, 'db') == {'host': 'localhost'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
