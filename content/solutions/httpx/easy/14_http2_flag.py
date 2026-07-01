import httpx

def client_no_http2():
    def handler(request):
        return httpx.Response(200)
    return httpx.Client(http2=False, transport=httpx.MockTransport(handler))
