# title: Retry Session
# track: requests
# difficulty: hard
# tags: requests, retry
# description: |
# Return a requests.Session mounted with an HTTPAdapter that retries up to 3 times on 500/502/503/504 with backoff 0.3. (No network call.)
# examples:
# adapter has max_retries=3
# hint: |
# from requests.adapters import HTTPAdapter; from urllib3.util.retry import Retry.
# syntax_hint: |
# Retry(total=3, backoff_factor=0.3, status_forcelist=[500,502,503,504])


def make_retry_session():
    pass


def run_tests() -> None:
    import requests
    from requests.adapters import HTTPAdapter
    s = make_retry_session()
    assert isinstance(s, requests.Session)
    adapter = s.get_adapter('https://x.test')
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 3
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
