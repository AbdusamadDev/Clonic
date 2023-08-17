from server import ClonicServer
from response import Response
from request import Request
from clonic import ClonicAPI


app = ClonicServer(("0.0.0.0", 8000), ClonicAPI)


def func(request: Request):
    print(request)

# @app.route("/hello", "GET")
# def hello(environ):  # renamed request to environ to match the caller in the App class
#     return Response(body=b'Hello motherfuckin world!', status="200 OK", headers=[("Content-Type", "text/plain")])


app.connect()
