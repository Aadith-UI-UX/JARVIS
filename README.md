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

## Milestone: First Memory Retrieval Prototype

**Date:** September 5, 2026

JARVIS's memory system was improved with a first-generation memory retrieval prototype.

### What was completed

- Created a dedicated conversation memory retrieval function.
- Added common-word filtering.
- Added basic relevance scoring based on shared words.
- Ranked matching conversations by relevance score.
- Combined relevant memories with recent conversation context.
- Removed duplicate conversation entries.
- Connected the retrieval system to the GPT gateway.
- Tested memory retrieval independently.
- Successfully tested the system through JARVIS's voice interface.

### Important Learning

The prototype showed that conversation history and permanent user facts should be treated differently.

For example, JARVIS already stores the user's name as permanent user memory. Searching old conversations for the user's name can produce duplicate or conflicting results.

The current retrieval system is therefore considered a prototype and will be improved in a future version.

### Current Status

JARVIS now has a basic memory retrieval layer that can select recent and potentially relevant conversation history before sending context to GPT.

Future versions may use more advanced semantic memory retrieval instead of simple word-based matching.

## Milestone: Memory Hierarchy

**Date:** September 7, 2026

JARVIS's memory system was improved by defining a hierarchy between permanent user memory and conversation memory.

### What was completed

- Separated permanent user memory from retrieved conversation context.
- Defined permanent user memory as the source of truth for stable user facts.
- Defined conversation memory as contextual information rather than authoritative information.
- Added an explicit memory hierarchy rule to the GPT prompt.
- Tested the system using conflicting memories.
- Verified that permanent user memory remains authoritative when conversation history contains conflicting information.
- Tested different phrasings of the same request, including:
  - "What is my name?"
  - "Tell me what you call me."
  - "Who am I?"

### Important Learning

JARVIS should provide GPT with both permanent memory and relevant conversation context when appropriate.

The Python layer manages and retrieves memory, while GPT handles natural-language understanding and response generation.

This allows JARVIS to understand differently phrased requests without requiring a separate hard-coded rule for every possible way the user can ask something.

### Current Limitation

The current conversation retrieval system is still based on simple word matching.

It can retrieve conversations containing related words, but it does not yet understand semantic similarity.

For example, requests such as "What is my name?" and "Who am I?" can have the same meaning to a human while producing different retrieval behavior.

Future versions may improve conversation retrieval using semantic memory techniques.

### Current Status

JARVIS now has a basic memory hierarchy in which permanent user memory is treated as authoritative while retrieved conversation history provides additional context.

The hierarchy has been tested successfully with conflicting memory and multiple user phrasings.

## Milestone: Reliability and Error Handling

**Date:** September 10, 2026

JARVIS's reliability was improved by adding basic error handling to both the speech recognition and AI communication layers.

### What was completed

- Added handling for speech recognition failures using `speech_recognition.UnknownValueError`.
- JARVIS now responds politely when it cannot understand spoken input.
- Added OpenAI API error handling using `OpenAIError`.
- JARVIS no longer crashes when the AI service cannot be reached.
- Added a user-friendly spoken response when the AI service fails.
- Prevented failed AI responses from being stored in conversation memory.
- Tested both speech-recognition failure and AI/API failure.
- Verified that JARVIS continues running after these failures.
- Restored and verified the normal GPT connection after testing.

### Important Learning

Different parts of JARVIS are responsible for different types of errors.

The speech layer handles problems understanding the user's voice, while `ai.py` handles technical failures from the AI service.

The main program, `jarvis.py`, is responsible for turning those failures into user-facing responses.

### Current Status

JARVIS can now gracefully handle two important failure cases:

1. Speech recognition failure.
2. AI/API communication failure.

Instead of crashing, JARVIS informs the user and continues operating.

## Milestone: Architecture Cleanup

**Date:** September 10, 2026

JARVIS's program structure was improved by separating reusable functions from the code that starts and runs the assistant.

### What was completed

- Added a protected main execution block using `if __name__ == "__main__":`.
- Prevented the JARVIS microphone loop from starting when `jarvis.py` is imported.
- Made reusable functions such as `clean_for_speech()` available without launching JARVIS.
- Created a temporary architecture test to verify the behavior.
- Confirmed that importing a JARVIS function does not start the assistant.

### Important Learning

Python files can contain reusable functions as well as executable program code.

The `if __name__ == "__main__":` pattern allows JARVIS to run its main program only when `jarvis.py` is launched directly, while still allowing its functions to be imported and reused elsewhere.

### Current Status

JARVIS's core program structure is now cleaner and more modular, providing a stronger foundation for future development.

## Milestone: Final v0.1 Audit

**Date:** September 10, 2026

JARVIS completed a final technical audit covering its core v0.1 functionality.

### Audit Results

- Startup and shutdown — PASS
- Speech recognition failure handling — PASS
- GPT communication — PASS
- JARVIS personality — PASS
- Permanent user memory — PASS
- Conversation memory and retrieval — PASS
- Speech output — PASS
- Architecture isolation — PASS
- Git repository integrity — PASS

### Final v0.1 Status

All planned core v0.1 functionality was tested successfully.

JARVIS can now:

- Interact through voice.
- Communicate with GPT.
- Follow its personality specification.
- Remember basic permanent user information.
- Store and retrieve conversation history.
- Retrieve relevant previous conversations.
- Handle basic speech-recognition and AI-service failures without crashing.
- Convert its AI responses into speech.
- Run with a cleaner, modular program structure.

### v0.1 Completion

JARVIS v0.1 is considered technically complete.

Future development will focus on more intelligent memory, improved memory organization, additional capabilities, and external tools. These features are intentionally reserved for later versions rather than expanding the v0.1 scope.