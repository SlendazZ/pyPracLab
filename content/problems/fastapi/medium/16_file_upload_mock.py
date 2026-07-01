# title: File Upload Mock Header
# track: fastapi
# difficulty: medium
# tags: fastapi, upload
# description: |
# Implement register(app) adding POST /upload reading filename from X-Filename header (mock upload metadata).
# examples:
# post with X-Filename: test.txt -> {'filename': 'test.txt'}
# hint: |
# Use Header(alias='X-Filename') instead of real multipart upload.
# syntax_hint: |
# from fastapi import Header; x_filename: str = Header(alias='X-Filename')


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    r = c.post('/upload', headers={'X-Filename': 'test.txt'})
    assert r.status_code == 200
    assert r.json() == {'filename': 'test.txt'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
