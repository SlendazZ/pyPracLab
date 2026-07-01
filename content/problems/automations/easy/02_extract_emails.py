# title: Extract Emails
# track: automations
# difficulty: easy
# tags: regex
# description: |
# Return all unique email-like addresses found in a text, in order of first appearance.
# examples:
# extract_emails("a@x.com b@y.com a@x.com") -> ["a@x.com","b@y.com"]
# hint: |
# re.findall with a simple email pattern; dedupe keeping order.
# syntax_hint: |
# pattern r'[\w.+-]+@[\w-]+\.[\w.-]+'


def extract_emails(text: str) -> list[str]:
    pass


def run_tests() -> None:
    assert extract_emails("a@x.com b@y.com a@x.com") == ["a@x.com", "b@y.com"]
    assert extract_emails("no emails here") == []
    assert extract_emails("reach eli.test@site.io") == ["eli.test@site.io"]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
