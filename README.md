# JARVIS

My personal AI assistant project.

## Current Version

**v0.1**

## About

JARVIS is a personal AI assistant that I am building from the ground up while learning programming and software development.

This project is both a working AI assistant and a learning project. I am documenting the process, decisions, mistakes, and lessons as JARVIS evolves.

## Project Structure

- `jarvis.py` — Main JARVIS program
- `brain.py` — JARVIS's core logic
- `ai.py` — AI/GPT interaction
- `brain_test.py` — Testing
- `personality.txt` — JARVIS personality configuration
- `memory.json` — Local memory file (not uploaded to GitHub)

## Learning

This project is helping me learn by building instead of only following tutorials.

Topics currently being explored:

- Python
- Programming fundamentals
- Git & GitHub
- APIs
- AI integration
- Software architecture

## Roadmap

JARVIS is actively being developed.

More capabilities will be added as I learn and build.

## Milestone: First GPT-Powered Voice Conversation

**Date:** September 4, 2026

JARVIS successfully completed its first full AI-powered voice conversation.

### What was completed

- Added the OpenAI Python SDK.
- Connected JARVIS to the OpenAI API through `ai.py`.
- Created the `ask_ai()` AI gateway function.
- Connected `personality.txt` to the AI gateway.
- Successfully tested GPT independently.
- Connected the AI response back to JARVIS.
- Successfully tested the complete voice pipeline.
- JARVIS can now:
  - Listen to the user through the microphone.
  - Convert speech to text.
  - Send the request to GPT.
  - Generate a response using the JARVIS personality.
  - Speak the response aloud.

### Current Architecture

```text
User
  ↓
Speech Recognition
  ↓
jarvis.py
  ↓
ai.py
  ↓
OpenAI API
  ↓
GPT
  ↓
JARVIS Personality
  ↓
jarvis.py
  ↓
Text-to-Speech
  ↓
User

### Current Status

JARVIS can now hold a basic voice conversation with GPT while using stored user information from `memory.json`.

The next step is to improve how JARVIS manages and uses conversation memory.

## Milestone: Memory-Enabled Voice Conversation

**Date:** September 4, 2026

JARVIS successfully used stored memory while having a voice conversation.

### What was completed

- Connected `memory.json` to the AI gateway.
- Updated `ai.py` to provide stored memory to GPT.
- Connected the existing JARVIS personality and memory together.
- Tested memory retrieval independently.
- Successfully tested memory retrieval through the microphone.
- JARVIS can now:
  - Listen to the user.
  - Access relevant stored information.
  - Use that information when generating a response.
  - Speak the response aloud.

### Example

The user asked:

> "What is my name?"

JARVIS retrieved the stored name from `memory.json` and responded:

> "Your name is Aadith Abhimanyu S, sir."

### Current Status

JARVIS can now hold a basic voice conversation with GPT while using stored user information from its local memory.

The next step is to improve how JARVIS manages and uses conversation memory.