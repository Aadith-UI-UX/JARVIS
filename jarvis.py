import json
import os
import speech_recognition as sr
import pyttsx3

from brain import think
from ai import ask_ai

# -----------------------------
# Load JARVIS personality
# -----------------------------

with open("personality.txt", "r", encoding="utf-8") as file:
    personality = file.read()


# -----------------------------
# Load JARVIS memory
# -----------------------------

MEMORY_FILE = "memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        memory = json.load(file)
else:
    memory = {
        "user": {},
        "conversation": []
    }


# -----------------------------
# Make sure memory has
# the correct structure
# -----------------------------

if "user" not in memory:
    memory["user"] = {}

if "conversation" not in memory:
    memory["conversation"] = []


# -----------------------------
# Save memory
# -----------------------------

def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


# -----------------------------
# Speech recognition
# -----------------------------

recognizer = sr.Recognizer()


# -----------------------------
# JARVIS voice
# -----------------------------

def speak(text):
    print("JARVIS:", text)

    jarvis = pyttsx3.init()
    jarvis.say(text)
    jarvis.runAndWait()
    jarvis.stop()


# -----------------------------
# Start JARVIS
# -----------------------------

speak("Good evening, sir. JARVIS is online.")


# -----------------------------
# Main conversation loop
# -----------------------------

while True:

    with sr.Microphone() as source:

        print("JARVIS: Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = recognizer.listen(source)

    try:

        # -----------------------------
        # Convert speech to text
        # -----------------------------

        text = recognizer.recognize_google(audio)

        print("You:", text)


        # -----------------------------
        # Correct common speech errors
        # -----------------------------

        corrections = {
            "Aditya Abhimanyu s": "Aadith Abhimanyu S",
            "Aditya Abhimanyu as": "Aadith Abhimanyu S",
            "Aditya Abhimanyu": "Aadith Abhimanyu",
            "Aditya": "Aadith",
            "aditya abhimanyu s": "Aadith Abhimanyu S",
            "aditya abhimanyu as": "Aadith Abhimanyu S",
            "aditya abhimanyu": "Aadith Abhimanyu",
            "aditya": "Aadith"
        }

        corrected_text = text

        for wrong, right in corrections.items():
            corrected_text = corrected_text.replace(wrong, right)

        print("JARVIS understood:", corrected_text)


        # -----------------------------
        # Normalize command
        # -----------------------------

        command = " ".join(corrected_text.lower().split())


        # -----------------------------
        # Goodbye / exit
        # -----------------------------

        if (
            "goodbye" in command
            or "good bye" in command
            or command == "exit"
            or command == "quit"
            or command == "shutdown"
        ):
            speak("Goodbye, sir.")
            break


        # -----------------------------
        # Remember user's name
        # -----------------------------

        elif "my name is" in command:

            name = corrected_text.split("my name is", 1)[1].strip()

            if name:

                if "name" in memory["user"]:

                    existing_name = memory["user"]["name"]

                    if name.lower() == existing_name.lower():

                        speak(
                            f"Yes, sir. I remember you as "
                            f"{existing_name}."
                        )

                    else:

                        speak(
                            "I already have your name stored, sir."
                        )

                else:

                    memory["user"]["name"] = name
                    save_memory()

                    speak(
                        f"I'll remember that, sir. "
                        f"Your name is {name}."
                    )


        # -----------------------------
        # JARVIS Brain
        # -----------------------------

        else:

            response = ask_ai(command, memory)

            speak(response)

            memory["conversation"].append({
                "user": corrected_text,
                "jarvis": response
            })

            save_memory()


    except sr.UnknownValueError:

        print("JARVIS: I didn't understand that.")


    except sr.RequestError:

        speak(
            "I am having trouble connecting "
            "to the speech recognition service."
        )