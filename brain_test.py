from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="You are JARVIS. Say hello to your creator in one short sentence."
)

print(response.output_text)