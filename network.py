import socket
import pickle
import struct

HEADERSIZE = 10


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.h_name = socket.gethostname()
        self.IP_address = socket.gethostbyname(self.h_name)
        self.server = self.IP_address

        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data, recv):
        try:
            self.client.send(str.encode(data))
            if recv is True:
                return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def send_data(self, data):
        data_to_send = pickle.dumps(data)
        data_size = bytes(f'{len(data_to_send):<{10}}', "utf-8")
        try:
            self.client.send(data_size + data_to_send)

            package = self.receive_data()
            return package
        except socket.error as e:
            print(e)

    def receive_data(self):
        global msglen
        full_msg = b''
        new_msg = True
        while True:
            msg = self.client.recv(16)
            if new_msg:
                # msglen = int(msg[:HEADERSIZE])
                # new_msg = False
                try:
                    msglen = int(msg[:HEADERSIZE])
                    new_msg = False
                except ValueError:
                    msglen = 0
                    new_msg = False

            full_msg += msg

            if len(full_msg) - HEADERSIZE == msglen:
                data = pickle.loads(full_msg[HEADERSIZE:])
                break

        return data
