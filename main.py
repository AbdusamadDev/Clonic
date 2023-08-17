from request import App
from response import Response

app = App()


@app.route("/hello", "GET")
def hello(environ):  # renamed request to environ to match the caller in the App class
    return Response(body=b'Hello motherfuckin world!', status="200 OK", headers=[("Content-Type", "text/plain")])


app.run()
