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

Current Status

The basic voice-based AI conversation loop is working.

The next major step is to connect JARVIS's existing memory system to the AI gateway so that GPT can use relevant information from memory.json when responding