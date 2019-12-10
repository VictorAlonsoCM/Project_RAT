import socket
import time

class Network:

    def __init__(self):
        self = self
        # Creating a socket object
        self.sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Set host IP and port
        self.host = socket.gethostname()
        self.port = 1337
        # self.sc.listen()
        # Receive no more than 1024 bytes
        # connection to hostname on port
        try:
            self.sc.connect((self.host, self.port))
        except (socket.error):
            print("No available to connect")

    def connectionRecv(self):
        try:
            msg = self.sc.recv(1024)
            #self.sc.close()
            return msg.decode("ascii")
        except (socket.error):
            print("No available to connect")

    def connectionSend(self, data):
        try: 
            self.sc.send(data)
        except (socket.error, OSError):
            print("No available to connect")

    def connectionClose(self):
        print("Connection lost")
        self.sc.close()
        time.sleep(1)