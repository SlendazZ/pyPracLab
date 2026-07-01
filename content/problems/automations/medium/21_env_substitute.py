# title: Env Substitute
# track: automations
# difficulty: medium
# tags: string
# description: |
# Replace ${VAR} in template with values from env dict; leave unknown as empty string.
# examples:
# substitute("hi ${NAME}", {"NAME":"Ada"}) -> "hi Ada"
# hint: |
# re.sub r'\$\{([^}]+)\}' lambda m: env.get(m.group(1),'').
# syntax_hint: |
# import re; re.sub(pattern, repl, template)


def substitute(template: str, env: dict[str, str]) -> str:
    pass


def run_tests() -> None:
    assert substitute("hi ${NAME}", {"NAME": "Ada"}) == "hi Ada"
    assert substitute("${X}-${Y}", {"X": "1"}) == "1-"
    assert substitute("plain", {}) == "plain"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
