class BankAccount:
    def __init__(self, balance: float = 0):
        self._bal = balance
    def deposit(self, amount: float) -> None:
        self._bal += amount
    def withdraw(self, amount: float) -> None:
        if amount > self._bal:
            raise ValueError('insufficient funds')
        self._bal -= amount
    def balance(self) -> float:
        return self._bal
