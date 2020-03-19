import pygame
import speech_recognition as sr
import pyaudio
import wave
from difflib import SequenceMatcher

class recording():
    def __init__(self):
        self.recorder = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)
            
    def record(self, target, name): 
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        WIDTH = 2
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 7
        WAVE_OUTPUT_FILENAME = name

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(WIDTH),
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK)

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)  #read audio stream
            frames.append(data)
            stream.write(data, CHUNK)  #play back audio stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        recorded = self.SpeechToText(name)
        
        return recorded

    def SpeechToText(self, name):
        audio = sr.AudioFile(name)
        message = ""
        try:
            with audio as source:
                audio = self.recorder.record(source)
                message = self.recorder.recognize_google(audio)
            #print("Check: "+message)
        except:
            pass
        return message

    def get_jaccard_sim(self, str1, str2): 
        a = set(str1.split()) 
        b = set(str2.split())
        c = a.intersection(b)
        return float(len(c)) / (len(a) + len(b) - len(c))


    def get_validated(self, text, sen):
        jac_sm = (self.get_jaccard_sim(text, sen) + SequenceMatcher(None, text, sen).ratio())/2
        if jac_sm > 0.48:
            return True #validated
        return False

