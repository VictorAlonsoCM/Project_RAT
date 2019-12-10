from socket import *
import socket
import selectors
from threading import *
import signal
import select
import queue


   
def send():
    while True:
        try:
            # establish a connection
            msg = input("Enter a value: ")
            
            print("Got a connection from %s" % str(addr))

            clientsocket.send(msg.encode("ascii"))
        except KeyboardInterrupt:
            break




# Set host IP and port
host = socket.gethostname()
port = 1337
# Create socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

# Any data sent to ssock shows up on rsock
rsock, ssock = socket.socketpair()

# Bind to the port
serversocket.bind((host, port))

# For this project the maximun allowed connection are 5
serversocket.listen(5)
clientsocket,addr = serversocket.accept()

send_queue = queue.Queue()

# Your callback thread
def different_thread():
    # Put the data to send inside the queue
    msg = input("Ingresa un valor").encode("ascii")
    send_queue.put(msg)

    # Trigger the main thread by sending data to ssock which goes to rsock
    ssock.send(b"\x00")


Thread(target=different_thread).start()
#event = threading.Event()
#Thread(target = receive).start()
#sel.register(serversocket, selectors.EVENT_READ, data = None)
#th.start()

    #data = clientsocket.recv(8192)
    #print(data.decode("utf-8"))

while True:
    # When either main_socket has data or rsock has data, select.select will return
    rlist, _, _ = select.select([clientsocket, rsock], [], [])
    for ready_socket in rlist:
        if ready_socket is clientsocket:
            data = clientsocket.recv(1024)
            # Do stuff with data, fill this up with your code
        else:
            # Ready_socket is rsock
            rsock.recv(1)  # Dump the ready mark
            # Send the data.
            clientsocket.sendall(send_queue.get())