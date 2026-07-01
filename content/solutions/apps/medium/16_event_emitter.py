class EventEmitter:
    def __init__(self):
        self._handlers: dict[str, list] = {}
    def on(self, event: str, handler) -> None:
        self._handlers.setdefault(event, []).append(handler)
    def off(self, event: str, handler) -> None:
        if event in self._handlers:
            self._handlers[event] = [h for h in self._handlers[event] if h is not handler]
    def emit(self, event: str, *args) -> None:
        for h in self._handlers.get(event, []):
            h(*args)
