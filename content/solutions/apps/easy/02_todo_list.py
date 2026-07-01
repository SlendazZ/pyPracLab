class TodoList:
    def __init__(self):
        self.items: list[dict] = []
    def add(self, task: str) -> None:
        self.items.append({'title': task, 'done': False})
    def complete(self, task: str) -> None:
        for t in self.items:
            if t['title'] == task and not t['done']:
                t['done'] = True
                return
    def pending(self) -> list[str]:
        return [t['title'] for t in self.items if not t['done']]
