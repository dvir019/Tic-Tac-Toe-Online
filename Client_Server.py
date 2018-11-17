import socket


class ClientServer(object):
    def __init__(self, sock, sign):
        self.sock = sock  # type: socket
        self.sign = sign  # type: str
