# -----------------------------
# JARVIS AI Interface v0.3
# -----------------------------


from openai import OpenAI, OpenAIError
import json

COMMON_WORDS = {
    "what",
    "is",
    "my",
    "the",
    "a",
    "an",
    "how",
    "are",
    "you",
    "i",
    "me",
    "to",
    "of",
    "in",
    "on",
    "do",
    "did"
}

client = OpenAI()


# -----------------------------
# Load JARVIS personality
# -----------------------------

with open("personality.txt", "r", encoding="utf-8") as file:
    personality = file.read()

# -----------------------------
# Find relevant conversation memory
# -----------------------------

def retrieve_relevant_memory(command, memory):

    recent_conversation = memory["conversation"][-10:]

    command_words = {
        word
        for word in command.lower().split()
        if word not in COMMON_WORDS
    }

    scored_conversations = []

    for conversation in memory["conversation"]:

        user_message = conversation.get("user", "").lower()

        message_words = {
            word
            for word in user_message.split()
            if word not in COMMON_WORDS
        }

        matching_words = command_words.intersection(message_words)

        score = len(matching_words)

        if score > 0:
            scored_conversations.append(
                (score, conversation)
            )

    scored_conversations.sort(
        key=lambda item: item[0],
        reverse=True
    )

    relevant_conversation = [
        conversation
        for score, conversation in scored_conversations
    ]

    combined_conversation = []

    for conversation in recent_conversation + relevant_conversation:

        if conversation not in combined_conversation:
            combined_conversation.append(conversation)

    return combined_conversation

def ask_ai(command, memory):

    relevant_conversation = retrieve_relevant_memory(command, memory)

    memory_for_ai = {
        "permanent_user_memory": memory["user"],
        "conversation_context": relevant_conversation
    }

    memory_text = json.dumps(memory_for_ai, indent=2)

    prompt = f"""
You are JARVIS, a personal AI assistant.

Here is your personality specification:

{personality}

Here is JARVIS's stored memory:

{memory_text}

The user said:

{command}

Permanent user memory is the source of truth for stable facts about the user.
Conversation context provides additional context and history.
Use conversation context when it is relevant to the user's request.
If conversation context conflicts with permanent user memory, trust the permanent user memory.
Do not invent memories or facts that are not present in the memory.
Respond as JARVIS according to the personality specification.
"""
    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

    except OpenAIError:
        return "ERROR"

    return response.output_text