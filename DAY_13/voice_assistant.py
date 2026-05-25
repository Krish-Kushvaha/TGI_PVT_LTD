import speech_recognition as sr
import pyttsx3
from datetime import datetime

voice_reader = sr.Recognizer()
speaker = pyttsx3.init()

def talk(message):
    print("AI Assistant:", message)
    speaker.say(message)
    speaker.runAndWait()

def hear():
    with sr.Microphone() as mic:
        print("Speak Something...")
        sound = voice_reader.listen(mic, timeout=5)
        text = voice_reader.recognize_google(sound)
        return text.lower()

talk("Hi! Your smart assistant is now active.")

while True:

    user_command = hear()

    if "time" in user_command:

        current_time = datetime.now().strftime("%I:%M %p")
        talk(f"Current time is {current_time}")

    elif "exit" in user_command:

        talk("Assistant is shutting down")
        break

    else:

        talk(f"I heard {user_command}")