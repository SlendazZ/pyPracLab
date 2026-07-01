import httpx

def client_with_cookies(cookies: dict):
    def handler(request):
        return httpx.Response(200, json={'ok': True})
    return httpx.Client(cookies=cookies, transport=httpx.MockTransport(handler))
