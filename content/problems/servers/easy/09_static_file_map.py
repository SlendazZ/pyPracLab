# title: Static File Map
# track: servers
# difficulty: easy
# tags: dict, mime
# description: |
# Given a list of filenames, return a dict mapping each name to a mime guessed from its extension ('.html'->'text/html', '.css'->'text/css', '.js'->'application/javascript', else 'application/octet-stream').
# examples:
# mimes(["a.html","b.css"]) -> {"a.html":"text/html","b.css":"text/css"}
# hint: |
# A small dict of extension -> mime does the job.
# syntax_hint: |
# ext = name.rsplit('.', 1)[-1] if '.' in name else ''


def mimes(names: list[str]) -> dict[str, str]:
    pass


def run_tests() -> None:
    assert mimes(["a.html", "b.css"]) == {"a.html": "text/html", "b.css": "text/css"}
    assert mimes(["app.js"]) == {"app.js": "application/javascript"}
    assert mimes(["noext"]) == {"noext": "application/octet-stream"}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
