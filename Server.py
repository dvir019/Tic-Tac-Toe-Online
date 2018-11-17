import socket

from Board import Board
from Client_Server import ClientServer


class Server(object):
    PORT = 4320

    def __init__(self):
        self.__socket = socket.socket()  # type: socket
        self.__socket.bind(('0.0.0.0', Server.PORT))
        self.__socket.listen(5)
        self.__clients = []  # type: list[ClientServer]
        self.__board = Board()  # type: Board

    def accept(self, client_number):
        if len(self.__clients >= 2):
            raise IndexError('There are already two clients')
        client_socket, client_addr = self.__socket.accept()
        if client_number == 1:
            self.__clients.append(ClientServer(client_socket, 'X' if client_number == 0 else 'O'))

    def receive(self, client_number):
        msg = self.__clients[client_number].sock.recv(1024)
        line, col = msg.split(',')
        self.__board[line, col] = self.__clients[client_number].sign

    def send(self, msg, client_number):
        try:
            self.__clients[client_number].sock.send(msg)
        except socket.error:
            print 'failed to send {} to client {}'.format(msg, client_number)

    def broadcast(self, msg):
        for i in xrange(len(self.__clients)):
            self.send(msg, i)
