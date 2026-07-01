# title: Split Path Segments
# track: servers
# difficulty: easy
# tags: string
# description: |
# Return the non-empty segments of a URL path, splitting on '/'.
# examples:
# segments("/a/b//c/") -> ["a","b","c"]
# hint: |
# Split on '/' and drop empty strings.
# syntax_hint: |
# [s for s in path.split('/') if s]


def segments(path: str) -> list[str]:
    pass


def run_tests() -> None:
    assert segments("/a/b//c/") == ["a", "b", "c"]
    assert segments("/") == []
    assert segments("/items/42") == ["items", "42"]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
