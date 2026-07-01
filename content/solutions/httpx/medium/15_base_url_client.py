import httpx

def get_status(base: str, path: str) -> int:
    def handler(request):
        return httpx.Response(200)
    with httpx.Client(base_url=base, transport=httpx.MockTransport(handler)) as client:
        return client.get(path).status_code
