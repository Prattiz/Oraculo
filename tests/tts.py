import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[-2].id) # -1 = english
engine.say("meu nome é oraculo")
engine.runAndWait()