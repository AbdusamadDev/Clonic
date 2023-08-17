from wsgiref.simple_server import make_server
from typing import Dict, Callable, Any
# from wsgiref.handlers import 


# class ClonicAPI:
#     def __init__(self) -> None:
#         self.media_path = None
#         self.headers = [("Content-Type", "text/plain")]
#         self.routes: Dict = {}

#     def __call__(self, environ, start_response) -> Any:
#         url = environ.get("PATH_INFO", "")
#         method = environ.get("REQUEST_METHOD", "")
#         handler = self.routes.get((url, method))

#         if handler:
#             response = handler(environ)
#             start_response(response.status, response.headers)
#             return [response.body]
#         else:
#             start_response("404 Not Found", self.headers)
#             return [b"Not Found"]

#     def get_headers(self):
#         return self.headers

#     def route(self, url, method):
#         def inner(func: Callable):
#             self.routes[(url, method)] = func

#         return inner

#     def run(self):
#         with make_server("127.0.0.1", 8000, app=self) as server:
#             print(
#                 "Server running on localhost: http://127.0.0.1:8000\nCtrl+C to quit the server"
#             )
#             server.serve_forever()

class ClonicAPI:
    def 