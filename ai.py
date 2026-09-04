# -----------------------------
# JARVIS AI Interface v0.3
# -----------------------------

from openai import OpenAI

client = OpenAI()


# -----------------------------
# Load JARVIS personality
# -----------------------------

with open("personality.txt", "r", encoding="utf-8") as file:
    personality = file.read()


# -----------------------------
# Ask AI
# -----------------------------

def ask_ai(command, memory):

    prompt = f"""
You are JARVIS, a personal AI assistant.

Here is your personality specification:

{personality}

The user said:

{command}

Respond as JARVIS according to the personality specification.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text