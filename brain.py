# -----------------------------
# JARVIS Brain v0.1
# -----------------------------

from datetime import datetime

def think(command, memory):

        # Greeting
    if (
        "hello" in command
        or "hi" in command
        or "hey" in command
        or "good morning" in command
        or "good afternoon" in command
        or "good evening" in command
    ):
        hour = datetime.now().hour

        if hour < 12:
            greeting = "Good morning"
        elif hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        return f"{greeting}, sir. How may I assist you?"

    # Name
    if "what is my name" in command:
        if "name" in memory["user"]:
            return f"Your name is {memory['user']['name']}, sir."

        return "I don't have your name stored yet, sir."

    # JARVIS identity
    if "your name" in command:
        return "I am JARVIS, sir."

    # Status
    if "how are you" in command:
        return "All systems are operational, sir."

    # Unknown
    return "I heard you, sir. I am still learning."