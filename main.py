from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
import core
import os

from nlu.classifier import classify



# Speech Synthesis

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id) # -1 = english

def speak(text):          
    engine.say(text)
    engine.runAndWait()

def evaluate(t):

    entity = classify(t)
        
    print('Text: {} Entity: {}'.format(t, entity))

    if entity == 'time|getTime':
        speak(core.SystemInfo.get_time())

    elif entity == 'time|getDate':
        speak(core.SystemInfo.get_date())

    elif entity == "open|notepad":
        speak('Abrindo o Bloco de Notas')
        os.system('notepad.exe')
        
    # more comands to make

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
        
        if text == "":
            speak("Desculpe, você falou algo?")
        else:
            evaluate(text)

        