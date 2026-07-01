# title: CASE WHEN Label
# track: sqlite
# difficulty: medium
# tags: sqlite, sql
# description: |
# Insert scores; return list of labels: 'pass' if score >= 60 else 'fail'.
# examples:
# label_scores([55, 70]) -> ['fail', 'pass']
# hint: |
# SELECT CASE WHEN score >= 60 THEN 'pass' ELSE 'fail' END
# syntax_hint: |
# CASE WHEN score >= 60 THEN 'pass' ELSE 'fail' END


def label_scores(scores: list[int]) -> list[str]:
    pass


def run_tests() -> None:
    assert label_scores([55, 70]) == ['fail', 'pass']
    assert label_scores([60]) == ['pass']
    assert label_scores([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
