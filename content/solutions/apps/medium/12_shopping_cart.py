class Cart:
    def __init__(self):
        self._items = []
    def add(self, name: str, price: float, qty: int) -> None:
        self._items.append((name, price, qty))
    def total(self) -> float:
        return sum(p * q for _, p, q in self._items)
