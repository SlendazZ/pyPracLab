# title: Contact Book
# track: apps
# difficulty: easy
# tags: oop
# description: |
# Implement a ContactBook with add_contact(name, email) and find_contact(name) -> dict or None. find is case-insensitive.
# examples:
# book.find("Alice") -> {"name": "Alice", "email": "a@x.com"}
# hint: |
# Store contacts as a list of dicts; lower-case the name when searching.
# syntax_hint: |
# class ContactBook: def __init__(self): self._contacts = []


class ContactBook:
    pass


def run_tests() -> None:
    book = ContactBook()
    book.add_contact("Alice", "a@x.com")
    book.add_contact("Bob", "b@x.com")
    assert book.find_contact("alice") == {"name": "Alice", "email": "a@x.com"}
    assert book.find_contact("BOB") == {"name": "Bob", "email": "b@x.com"}
    assert book.find_contact("nobody") is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
