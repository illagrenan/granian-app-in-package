# -*- encoding: utf-8 -*-
# ! python3

from test_app.logic import is_number_correct


async def app(scope, receive, send):
    some_number = 12
    print(f"Is number correct? {is_number_correct(some_number)}")

    assert scope["type"] == "http"

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"Hello, world!",
        }
    )
