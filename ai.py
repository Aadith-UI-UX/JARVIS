# -----------------------------
# JARVIS AI Interface v0.2
# -----------------------------

from openai import OpenAI

client = OpenAI()


def ask_ai(command, memory):

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=command
    )

    return response.output_text