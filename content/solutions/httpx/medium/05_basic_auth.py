import httpx

def make_auth_client(user: str, password: str):
    def handler(request):
        return httpx.Response(200, json={'ok': True})
    return httpx.Client(
        auth=(user, password),
        transport=httpx.MockTransport(handler),
    )
