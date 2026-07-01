import httpx

def make_timeout(connect: float, read: float):
    return httpx.Timeout(connect=connect, read=read, write=read, pool=connect)
