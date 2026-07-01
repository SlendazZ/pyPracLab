import httpx

def fetch_with_hook(url: str) -> list[str]:
    log: list[str] = []
    def on_request(request):
        log.append(request.method)
    def handler(request):
        return httpx.Response(200)
    with httpx.Client(
        transport=httpx.MockTransport(handler),
        event_hooks={'request': [on_request]},
    ) as client:
        client.get(url)
    return log
