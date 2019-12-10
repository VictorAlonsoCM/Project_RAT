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