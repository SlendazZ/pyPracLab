# title: Retry on Status Codes
# track: httpx
# difficulty: hard
# tags: httpx, retry
# description: |
# Using httpx.Client with MockTransport, retry a GET up to max_attempts times when the response status is in retry_statuses. Return the final response status code.
# examples:
# retry_get(client_fn, 503, 200) -> 200 after retries
# hint: |
# Loop up to max_attempts; on retryable status, continue; return last response.
# syntax_hint: |
# for attempt in range(max_attempts): r = client.get(url); if r.status_code not in retry_statuses: return r.status_code


def retry_get(client, url: str, max_attempts: int, retry_statuses: set[int]) -> int:
    pass


def run_tests() -> None:
    import httpx
    calls = {'n': 0}
    def handler(request):
        calls['n'] += 1
        if calls['n'] < 3:
            return httpx.Response(503)
        return httpx.Response(200)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        code = retry_get(client, 'https://x.test/api', 5, {503})
    assert code == 200
    assert calls['n'] == 3
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
