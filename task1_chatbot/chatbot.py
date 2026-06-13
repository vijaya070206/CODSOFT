"""
CodSoft AI Internship - Task 1
Rule-Based Chatbot using Pattern Matching
Author: Bandi Vijaya Siva Sai Naga Jyothi
"""

import re
import random

# ─────────────────────────────────────────────
# Pattern-Response Rules
# Each rule: (compiled regex, list of responses)
# ─────────────────────────────────────────────
RULES = [
    # Greetings
    (re.compile(r"\b(hi|hello|hey|howdy|hola|greetings)\b", re.IGNORECASE),
     ["Hello! How can I help you today?",
      "Hey there! What's on your mind?",
      "Hi! Nice to meet you. How can I assist?"]),

    # How are you
    (re.compile(r"\b(how are you|how do you do|how's it going|how are things)\b", re.IGNORECASE),
     ["I'm doing great, thanks for asking! How about you?",
      "All systems running perfectly! What can I do for you?",
      "I'm just a bot, but I feel fantastic! How can I help?"]),

    # Name
    (re.compile(r"\b(what is your name|who are you|what('s| is) your name)\b", re.IGNORECASE),
     ["I'm ChatBot, your AI assistant built for CodSoft!",
      "My name is ChatBot. I'm here to assist you."]),

    # What can you do
    (re.compile(r"\b(what can you do|help me|what do you know|your capabilities)\b", re.IGNORECASE),
     ["I can answer general questions, tell jokes, give the time, discuss AI topics, and chat with you!",
      "I can help with: general knowledge, jokes, AI info, greetings, and basic conversation."]),

    # Jokes
    (re.compile(r"\b(tell me a joke|joke|make me laugh|say something funny)\b", re.IGNORECASE),
     ["Why do programmers prefer dark mode? Because light attracts bugs! 😄",
      "Why did the robot go on a diet? It had too many bytes! 🤖",
      "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 😂",
      "Why was the math book sad? It had too many problems!"]),

    # AI topic
    (re.compile(r"\b(what is ai|artificial intelligence|machine learning|deep learning|neural network)\b", re.IGNORECASE),
     ["AI (Artificial Intelligence) is the simulation of human intelligence in machines. It includes ML, DL, NLP, and more.",
      "Machine Learning is a subset of AI where systems learn from data to improve performance.",
      "Deep Learning uses neural networks with many layers to learn complex patterns from large datasets."]),

    # Time
    (re.compile(r"\b(what time is it|current time|tell me the time)\b", re.IGNORECASE),
     ["__TIME__"]),  # placeholder handled in get_response()

    # Date
    (re.compile(r"\b(what('s| is) (the |today's )?date|what day is it|today('s)? date)\b", re.IGNORECASE),
     ["__DATE__"]),  # placeholder handled in get_response()

    # Feeling sad
    (re.compile(r"\b(i('m| am) (sad|depressed|upset|unhappy|not okay|not good)|i feel (bad|sad|down))\b", re.IGNORECASE),
     ["I'm sorry to hear that. Remember, it's okay to not be okay sometimes. Things will get better! 💙",
      "That's tough. Take a deep breath — you've got this! 😊"]),

    # Feeling happy
    (re.compile(r"\b(i('m| am) (happy|great|good|awesome|wonderful|excited)|i feel (good|great|amazing))\b", re.IGNORECASE),
     ["That's wonderful to hear! Keep that energy going! 🎉",
      "Awesome! Positivity is contagious. What made your day great?"]),

    # Favourite food
    (re.compile(r"\b(favourite food|favorite food|what do you eat|do you eat)\b", re.IGNORECASE),
     ["I'm a bot so I don't eat, but I've heard pizza and biryani are crowd favourites! 🍕🍛"]),

    # Age
    (re.compile(r"\b(how old are you|your age|when were you born|what('s| is) your age)\b", re.IGNORECASE),
     ["I'm ageless — I was created recently and I'm always learning!",
      "I don't have an age, but I was just born into this terminal!"]),

    # Creator / who made you
    (re.compile(r"\b(who made you|who created you|who built you|your creator|who is your developer)\b", re.IGNORECASE),
     ["I was built by Jyothi as part of the CodSoft AI Internship Task 1!",
      "A CSE student named Jyothi created me for the CodSoft internship. Pretty cool, right?"]),

    # Weather
    (re.compile(r"\b(weather|temperature|will it rain|is it hot|is it cold)\b", re.IGNORECASE),
     ["I don't have live weather data yet, but you can check weather.com or Google for accurate info!",
      "For real-time weather, try asking Google Assistant or checking your phone's weather app!"]),

    # Thank you
    (re.compile(r"\b(thank you|thanks|thx|thank u|ty)\b", re.IGNORECASE),
     ["You're welcome! Happy to help anytime. 😊",
      "No problem at all! Feel free to ask anything.",
      "Glad I could help!"]),

    # Goodbye
    (re.compile(r"\b(bye|goodbye|see you|see ya|exit|quit|later|farewell)\b", re.IGNORECASE),
     ["Goodbye! Have a wonderful day! 👋",
      "See you later! Take care!",
      "Bye! It was nice chatting with you. Come back anytime!"]),
]

# ─────────────────────────────────────────────
# Default fallback responses
# ─────────────────────────────────────────────
FALLBACK_RESPONSES = [
    "I'm not sure I understand that. Could you rephrase?",
    "Hmm, that's a tricky one. Try asking me something else!",
    "I don't have an answer for that yet. I'm still learning!",
    "Interesting question! I'm not sure about that one.",
]


def get_response(user_input: str) -> str:
    """
    Match user input against patterns and return a response.
    Returns a fallback if no pattern matches.
    """
    from datetime import datetime

    for pattern, responses in RULES:
        if pattern.search(user_input):
            response = random.choice(responses)

            # Handle dynamic placeholders
            if response == "__TIME__":
                return f"The current time is {datetime.now().strftime('%I:%M %p')}."
            if response == "__DATE__":
                return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

            return response

    return random.choice(FALLBACK_RESPONSES)


def run_chatbot():
    """
    Main loop — reads user input and prints bot response.
    Type 'bye', 'exit', or 'quit' to stop.
    """
    print("=" * 55)
    print("       Welcome to ChatBot — CodSoft AI Task 1")
    print("       Type 'bye' or 'exit' to end the chat.")
    print("=" * 55)

    EXIT_WORDS = re.compile(r"\b(bye|goodbye|exit|quit|farewell|see you)\b", re.IGNORECASE)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please type something so I can help you!")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        # End session on farewell
        if EXIT_WORDS.search(user_input):
            break


if __name__ == "__main__":
    run_chatbot()
