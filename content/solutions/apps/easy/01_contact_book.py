class ContactBook:
    def __init__(self):
        self._contacts: list[dict] = []
    def add_contact(self, name: str, email: str) -> None:
        self._contacts.append({'name': name, 'email': email})
    def find_contact(self, name: str):
        target = name.lower()
        for c in self._contacts:
            if c['name'].lower() == target:
                return c
        return None
