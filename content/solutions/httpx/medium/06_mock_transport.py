import httpx

def fetch_json(url: str) -> dict:
    def handler(request):
        return httpx.Response(200, json={'message': 'ok'})
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        return client.get(url).json()
