import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Select female voice if available
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
