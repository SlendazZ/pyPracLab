def compose(middlewares: list, final):
    handler = final
    for mw in reversed(middlewares):
        def make(mw=mw, h=handler):
            def wrapped(req):
                return mw(req, h)
            return wrapped
        handler = make()
    return handler
