# title: Event Emitter
# track: apps
# difficulty: medium
# tags: oop, events
# description: |
# Implement EventEmitter with on(event, handler), off(event, handler), and emit(event, *args) calling all handlers.
# examples:
# em.on('x', fn); em.emit('x', 1) calls fn(1)
# hint: |
# Store handlers per event in a list of callables.
# syntax_hint: |
# self._handlers: dict[str, list] = {}


class EventEmitter:
    pass


def run_tests() -> None:
    em = EventEmitter()
    log = []
    em.on('x', lambda v: log.append(v))
    em.emit('x', 42)
    assert log == [42]
    fn = lambda: log.append(1)
    em.on('y', fn); em.off('y', fn); em.emit('y')
    assert log == [42]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
