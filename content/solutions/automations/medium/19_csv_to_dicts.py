import csv
import io

def csv_dicts(text: str) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(text)))
