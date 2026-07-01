# title: CSV Expense Summary
# track: automations
# difficulty: easy
# tags: csv, io
# description: |
# Given CSV text with columns 'item,amount', return the total of the amounts as a float.
# examples:
# total_expenses("item,amount\nA,1.5\nB,2.5") -> 4.0
# hint: |
# csv.DictReader over an io.StringIO of the text.
# syntax_hint: |
# import csv, io; for row in csv.DictReader(io.StringIO(text)): sum += float(row['amount'])


def total_expenses(text: str) -> float:
    pass


def run_tests() -> None:
    assert total_expenses("item,amount\nA,1.5\nB,2.5") == 4.0
    assert total_expenses("item,amount\nX,10") == 10.0
    assert total_expenses("item,amount\n") == 0.0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
