from .brain import ask_brain
from .voice import speak


def run(input_source=input):
    speak("नमस्ते Kanak, मैं वैष्णवी बॉट हूँ।")

    while True:
        user_input = input_source("You: ")

        if user_input.lower() == "exit":
            speak("फिर मिलेंगे।")
            break

        reply = ask_brain(user_input)
        print("VaishnaviBot:", reply)
        speak(reply)


if __name__ == "__main__":
    run()
