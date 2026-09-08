try:
    import pyttsx3

    try:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        if voices and len(voices) > 1:
            engine.setProperty("voice", voices[1].id)
    except Exception:
        engine = None
except ImportError:
    engine = None


def speak(text):
    if engine is not None:
        try:
            engine.say(text)
            engine.runAndWait()
            return
        except Exception:
            pass
    print(f"[VOICE]: {text}")
