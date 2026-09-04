# -----------------------------
# JARVIS AI Interface v0.3
# -----------------------------


from openai import OpenAI
import json

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

    memory_text = json.dumps(memory, indent=2)

    prompt = f"""
You are JARVIS, a personal AI assistant.

Here is your personality specification:

{personality}

Here is JARVIS's stored memory:

{memory_text}

The user said:

{command}

Use the stored memory when it is relevant.
Do not invent memories or facts that are not present in the memory.
Respond as JARVIS according to the personality specification.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text