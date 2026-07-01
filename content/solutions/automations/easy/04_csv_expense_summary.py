import csv
import io

def total_expenses(text: str) -> float:
    total = 0.0
    for row in csv.DictReader(io.StringIO(text)):
        total += float(row['amount'])
    return total
