# Task 1 — Rule-Based Chatbot

**CodSoft AI Internship**

## Overview
A simple chatbot built in Python that responds to user inputs using predefined rules. It uses `re` (regex) for pattern matching — no external libraries required.

## Features
- Greetings and farewells
- General conversation (feelings, jokes, name, age)
- AI/ML topic responses
- Live time and date display
- Friendly fallback for unknown inputs
- Random response variation (multiple responses per pattern)

## How to Run

```bash
python chatbot.py
```

No pip installs needed — uses only Python's built-in `re` and `datetime`.

## Sample Conversation

```
You: hi
Bot: Hello! How can I help you today?

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄

You: what is AI?
Bot: AI (Artificial Intelligence) is the simulation of human intelligence in machines.

You: what time is it
Bot: The current time is 10:45 AM.

You: bye
Bot: Goodbye! Have a wonderful day! 👋
```

## Tech Used
- Python 3.x
- `re` module (regex pattern matching)
- `random` module (response variation)
- `datetime` module (live time/date)

## Author
Bandi Vijaya Siva Sai Naga Jyothi  
CodSoft AI Internship — Task 1
