from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
import core

from nlu.classifier import classify

# Speech Synthesis

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id) # -1 = english

def speak(text):          
    engine.say(text)
    engine.runAndWait()


model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        text = result['text']

        entity = None
        entity = classify(text)
        
        print('Text: {} Entity: {}'.format(text, entity))
        if entity == 'time\getTime':
            speak(core.SystemInfo.get_time())

        