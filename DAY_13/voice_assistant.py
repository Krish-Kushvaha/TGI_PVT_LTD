import speech_recognition as sr
import pyttsx3
from datetime import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():

    try:
        with sr.Microphone() as source:

            print("Listening...")

            listener.adjust_for_ambient_noise(source)

            audio = listener.listen(source, timeout=5)

            command = listener.recognize_google(audio)

            return command.lower()

    except Exception as error:

        print("Error:", error)

        return ""

speak("Voice assistant started")

while True:

    user_text = listen()

    if "time" in user_text:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"Current time is {current_time}")

    elif "exit" in user_text:

        speak("Goodbye")
        break

    elif user_text != "":

        speak(f"You said {user_text}")