def retry_get(client, url: str, max_attempts: int, retry_statuses: set[int]) -> int:
    last = 0
    for _ in range(max_attempts):
        response = client.get(url)
        last = response.status_code
        if last not in retry_statuses:
            return last
    return last
