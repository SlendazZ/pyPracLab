# title: Bank Account
# track: apps
# difficulty: medium
# tags: class
# description: |
# BankAccount with deposit, withdraw (no overdraft), and balance.
# examples:
# a=BankAccount(100); a.withdraw(30); a.balance() -> 70
# hint: |
# Reject withdraw if amount > balance.
# syntax_hint: |
# if amount > self._bal: raise ValueError


class BankAccount:
    def __init__(self, balance: float = 0): pass
    def deposit(self, amount: float) -> None: pass
    def withdraw(self, amount: float) -> None: pass
    def balance(self) -> float: pass


def run_tests() -> None:
    a = BankAccount(100)
    a.withdraw(30)
    assert a.balance() == 70
    a.deposit(10)
    assert a.balance() == 80
    try:
        a.withdraw(100)
        assert False
    except ValueError:
        pass
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
