# title: Cache Key Builder
# track: apis
# difficulty: easy
# tags: cache, url
# description: |
# Build a cache key from url and params dict: url + '?' + sorted query string.
# examples:
# cache_key('https://x.test', {'b':2,'a':1}) -> 'https://x.test?a=1&b=2'
# hint: |
# Sort param keys; urllib.parse.urlencode.
# syntax_hint: |
# from urllib.parse import urlencode; f'{url}?{urlencode(sorted(params.items()))}'


def cache_key(url: str, params: dict) -> str:
    pass


def run_tests() -> None:
    assert cache_key('https://x.test', {'b': 2, 'a': 1}) == 'https://x.test?a=1&b=2'
    assert cache_key('https://x.test', {}) == 'https://x.test'
    assert 'q=py' in cache_key('https://x.test/api', {'q': 'py'})
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
