from socketserver import BaseRequestHandler, BaseServer
import json


class Request(BaseRequestHandler):
    """Base Class for handling Requests coming from HTTP Client"""

    def __init__(self, request, client_address, server: BaseServer) -> None:
        self.url = None
        self.data = None
        self.json = None
        self.method = None
        self.protocol = None
        # self.form_data = {}
        self.headers = {}
        super().__init__(request, client_address, server)

    def __str__(self) -> str:
        return f"<{type(self)}>: {self.__class__.__name__}"

    def handle(self) -> None:
        """
        Hanlding the data coming from client no matter what method request is
        """
        self.data = self.request.recv(4096).decode("utf-8")
        self.parse_request(self.data)
        print(self.json)
        print(self.url)
        # print(self.form_data)
        print(self.protocol)
        print(self.headers)
        print(self.method)

    def parse_request(self, data):
        """Parse each data like headers, body, http method of the coming request from client"""

        lines = data.split("\r\n")
        start_line = lines[0].split()

        self.method = start_line[0]
        self.url = start_line[1]
        self.protocol = start_line[2]

        # Parsing headers
        for line in lines[1:]:
            if line == '':
                break  # Headers are done, body will follow
            key, value = line.split(': ', 1)
            self.headers[key] = value

        # If there's JSON data (POST, PUT requests), parse it
        body = "\r\n".join(lines[len(self.headers) + 2:])
        print("Body: ", body)
        if body and 'Content-Type' in self.headers and self.headers['Content-Type'] == 'application/json':
            self.json = json.loads(body)
        # else:
        #     self.form_data = {
        #         "data": str(body.split("Content-Disposition: form-data; "))
        #     }
