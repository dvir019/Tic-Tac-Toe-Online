import socket

# the first message sent to the client is 'X' or 'O'
# all other messages is two numbers with a comma, 'winn', 'lose' or 'tie'


class Client(object):
    ip = "server's ip"
    port = 4320

    def __init__(self):
        self.__socket = socket.socket()  # type: socket
        self.connect()

    def connect(self):
        self.__socket.connect((Client.ip, Client.port))

    def send(self, msg):
        try:
            self.__socket.send(msg)
        except socket.error:
            print "can't send {}".format(msg)

    def receive(self):
        msg = self.__socket.recv(1024)
        return msg

