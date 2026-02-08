from voice import speak
from brain import ask_brain

def run():
    speak("नमस्ते Kanak, मैं वैष्णवी बॉट हूँ।")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            speak("फिर मिलेंगे।")
            break

        reply = ask_brain(user_input)
        print("VaishnaviBot:", reply)
        speak(reply)

if __name__ == "__main__":
    run()
