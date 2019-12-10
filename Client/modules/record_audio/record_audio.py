import os
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import calendar
import time


#import soundcard as sc
#import numpy

class Audio:

    def __init__(self):
        self = self

    def start_recording_audio(self, nt):
        fs = 44100  # Sample rate
        seconds = 10  # Duration of recording
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2) # Start recording
        sd.wait()  # Wait until recording is finished
        path = os.getcwd() # Get location Path
        directory = "\captures\\" # Costom directory
        print(path)
        ts = path+'\\'+str(calendar.timegm(time.gmtime())) # Get timesmap for naming the images
        print(ts)
        write('data.wav', fs, recording)  # Save as WAV file
        self.sendFile(ts, nt)

        return "Recording audio for 10 seconds\r\n"
        #write(str(ts), fs, recording)  # Save as WAV file

        # used to send files
    def sendFile(self, ts, nt):
        filename = "data.wav" # timestamp file
        f = open(ts, "rb") # open the file
        l = f.read(1024) # read the file
        while (l):
            nt.connectionSend(l) # send the content of the file
            l = f.read(1024) # read more data
        f.close() # close the file
        nt.connectionClose() # close the connection



    def start_recording_audio_not_tested(self):
        fs = 44100  # Sample rate
        seconds = 10  # Duration of recording
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2) # Start recording
        sd.wait()  # Wait until recording is finished
        path = os.getcwd() # Get location Path
        directory = "\captures\\" # Custom directory
        ts = path+directory+str(calendar.timegm(time.gmtime())) # Get timesmap for naming the images
        write(ts+'.wav', fs, recording)  # Save as WAV file
        
        # sound = AudioSegment.from_wav(ts)
        # sound.export(ts+'.mp3', format='mp3')
