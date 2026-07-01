from fastapi import Header

def register(app) -> None:
    @app.post('/upload')
    def upload(x_filename: str = Header(alias='X-Filename')):
        return {'filename': x_filename}
