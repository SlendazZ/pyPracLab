# title: CSV to Dicts
# track: automations
# difficulty: medium
# tags: csv
# description: |
# Parse CSV text with header row into list of dicts (strings).
# examples:
# csv_dicts("a,b\n1,2") -> [{"a":"1","b":"2"}]
# hint: |
# csv.DictReader over io.StringIO.
# syntax_hint: |
# import csv, io; list(csv.DictReader(io.StringIO(text)))


def csv_dicts(text: str) -> list[dict[str, str]]:
    pass


def run_tests() -> None:
    assert csv_dicts("a,b\n1,2") == [{"a": "1", "b": "2"}]
    assert csv_dicts("x\ny") == [{"x": "y"}]
    assert csv_dicts("h\n") == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
