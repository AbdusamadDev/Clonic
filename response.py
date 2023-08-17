from typing import Any


class Response:
    def __init__(self, body: str, status: Any, headers: list) -> None:
        self.body = body.encode("utf-8")
        self.status = status
        self.headers = headers

    def __iter__(self):
        yield self.body


if __name__ == "__main__":
    print(Response("asdsad", 200, ["asdasd", "asdasd"]))
