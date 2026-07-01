# title: JWT Payload Decode
# track: apis
# difficulty: medium
# tags: jwt, base64
# description: |
# Decode the payload section of a JWT string (no signature verification) and return the claims dict.
# examples:
# decode_payload("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0In0.sig") -> {"sub": "1234"}
# hint: |
# Split on '.'; base64url-decode the middle segment; json.loads.
# syntax_hint: |
# payload + '=' * (-len(payload) % 4); base64.urlsafe_b64decode


def decode_payload(token: str) -> dict:
    pass


def run_tests() -> None:
    tok = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0In0.sig"
    assert decode_payload(tok) == {'sub': '1234'}
    tok2 = "a.eyJuYW1lIjoiZWxpIn0.b"
    assert decode_payload(tok2) == {'name': 'eli'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
