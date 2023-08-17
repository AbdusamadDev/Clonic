from socketserver import TCPServer
from request import Request


class ClonicServer(TCPServer):
    """Connection of server with keeping alive until termination"""

    def connect(self):
        print(
            f"[INFO]: Clonic Server initiated\n[INFO]: Running on host: http://{self.server_address[0]}:{self.server_address[-1]}\n[INFO]: Ctrl+c to quit the server"
        )
        self.serve_forever()


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    clonic = ClonicServer((host, port), Request)

    clonic.connect()
