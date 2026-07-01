import httpx

def client_follow():
    def handler(request):
        return httpx.Response(200, json={'ok': True})
    return httpx.Client(
        follow_redirects=True,
        transport=httpx.MockTransport(handler),
    )
