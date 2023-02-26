import socket


class Network(object):
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.231.141"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.connect()

    def connect(self):
        self.client.connect(self.addr)

    def disconnect(self):
        self.client.shutdown(2)
        self.client.detach()
        self.client.close()

    def send(self, data):
        self.client.send(data.encode())

    def receive(self):
        return self.client.recv(4096).decode()
