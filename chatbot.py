import random
import datetime
import json
import os
from typing import Dict, List, Tuple

class BasicChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.user_name = None
        self.conversation_history = []
        self.learning_mode = False
        self.new_responses = {}

        self.responses = {
            "greetings": {
                "patterns": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
                "responses": [
                    "Hello! How can I help you today?",
                    "Hi there! Nice to meet you!",
                    "Hey! How's it going?",
                    "Greetings! I'm here to assist you.",
                    "Hello! What can I do for you?"
                ]
            },
            "farewells": {
                "patterns": ["bye", "goodbye", "see you", "exit", "quit", "cya"],
                "responses": [
                    "Goodbye! Have a great day!",
                    "See you later! Take care!",
                    "Bye! Feel free to come back anytime.",
                    "Goodbye! It was nice chatting with you!",
                    "Farewell! Hope to see you again soon!"
                ]
            },
            "how_are_you": {
                "patterns": ["how are you", "how do you do", "how's it going", "what's up"],
                "responses": [
                    "I'm doing great, thank you! How about you?",
                    "I'm fine, thanks for asking! And you?",
                    "All systems are functioning properly! How are you doing?",
                    "I'm good! Ready to help. How about yourself?"
                ]
            },
            "user_state": {
                "patterns": ["i'm", "i am", "i feel", "feeling"],
                "responses": [
                    "I see. Tell me more about that.",
                    "That is interesting. How does that make you feel?",
                    "I understand. Would you like to talk about it?",
                    "Thanks for sharing that with me."
                ]
            },
            "thanks": {
                "patterns": ["thank you", "thanks", "thx", "appreciate it"],
                "responses": [
                    "You are welcome!",
                    "My pleasure!",
                    "Happy to help!",
                    "Anytime! That is what I am here for."
                ]
            },
            "name": {
                "patterns": ["what is your name", "who are you", "your name"],
                "responses": [
                    f"I'm {self.name}, your friendly chatbot!",
                    f"You can call me {self.name}!",
                    f"I'm {self.name}, nice to meet you!",
                    f"My name is {self.name}. What is yours?"
                ]
            },
            "help": {
                "patterns": ["help", "what can you do", "capabilities", "functions"],
                "responses": [
                    "I can chat with you about many topics. Try asking me about:",
                    "I am here to have conversations with you. You can:",
                    "Here is what I can help you with:"
                ]
            },
            "time": {
                "patterns": ["what time is it", "current time", "time now", "what's the time"],
                "responses": [
                    "Let me check the time for you...",
                    "According to my clock...",
                    "The current time is..."
                ]
            },
            "date": {
                "patterns": ["what is the date", "today's date", "current date", "date today"],
                "responses": [
                    "Let me check the date...",
                    "Today's date is...",
                    "According to the calendar..."
                ]
            },
            "jokes": {
                "patterns": ["tell me a joke", "joke", "make me laugh", "funny"],
                "responses": [
                    "Why do not scientists trust atoms? Because they make up everything!",
                    "Why did the scarecrow win an award? He was outstanding in his field!",
                    "What do you call a bear with no teeth? A gummy bear!",
                    "Why do not eggs tell jokes? They would crack each other up!",
                    "I am reading a book on anti gravity. It is impossible to put down!"
                ]
            },
            "weather": {
                "patterns": ["weather", "how is the weather", "is it raining", "temperature"],
                "responses": [
                    "I would love to check the weather for you, but I need an internet connection for that!",
                    "For weather updates, you might want to check a weather app or site.",
                    "I am not connected to weather services, but I hope it is nice where you are!"
                ]
            },
            "default": {
                "patterns": [],
                "responses": [
                    "I am not sure I understand. Can you rephrase that?",
                    "That is interesting. Tell me more!",
                    "I see. Could you elaborate on that?",
                    "I am still learning. Could you say that differently?",
                    "I want to understand you better. Can you explain in another way?"
                ]
            }
        }

        self.help_topics = [
            "Say hello, hi, or hey to start chatting",
            "Ask how are you to check on me",
            "Say what can you do to see my functions",
            "Ask what time is it or what is the date",
            "Say tell me a joke",
            "Type bye, exit, or quit to end chat",
            "Say save chat to store our conversation",
            "Type learn mode to teach me new responses",
            "Say clear history to reset"
        ]

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower().strip()
        self.conversation_history.append({"user": user_input, "time": datetime.datetime.now()})

        special_response = self._check_special_commands(user_input)
        if special_response:
            return special_response

        if user_input in self.new_responses:
            return random.choice(self.new_responses[user_input])

        for category, data in self.responses.items():
            for pattern in data["patterns"]:
                if pattern in user_input:
                    response = random.choice(data["responses"])

                    if category == "time":
                        current_time = datetime.datetime.now().strftime("%I:%M %p")
                        response += f" It is {current_time}."
                    elif category == "date":
                        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
                        response += f" Today is {current_date}."
                    elif category == "name" and self.user_name:
                        response += f" I remember you are {self.user_name}!"
                    elif category == "help":
                        response += "\n" + "\n".join(self.help_topics)

                    return response

        return random.choice(self.responses["default"]["responses"])

    def _check_special_commands(self, user_input: str) -> str:
        user_input = user_input.lower()

        if user_input.startswith("my name is"):
            self.user_name = user_input.replace("my name is", "").strip().title()
            if self.user_name:
                return f"Nice to meet you, {self.user_name}! I will remember that."

        elif user_input == "learn mode":
            self.learning_mode = not self.learning_mode
            status = "ON" if self.learning_mode else "OFF"
            return f"Learning mode is now {status}. When ON, you can teach me new responses by typing when I say X, you say Y"

        elif self.learning_mode and "when i say" in user_input and "you say" in user_input:
            try:
                parts = user_input.split("when i say")[1].split("you say")
                trigger = parts[0].strip().lower()
                response = parts[1].strip()

                if trigger and response:
                    if trigger not in self.new_responses:
                        self.new_responses[trigger] = []
                    self.new_responses[trigger].append(response)
                    return f"Got it. When you say {trigger}, I will say {response}"
            except:
                pass

        elif user_input == "save chat":
            return self.save_conversation()

        elif user_input == "clear history":
            self.conversation_history.clear()
            return "Conversation history cleared. Starting fresh."

        elif user_input == "show history":
            if not self.conversation_history:
                return "No conversation history yet."

            history_text = "Our conversation so far:\n"
            for i, entry in enumerate(self.conversation_history[-10:], 1):
                time_str = entry["time"].strftime("%H:%M")
                history_text += f"{i}. [{time_str}] You: {entry['user']}\n"

            return history_text

        elif user_input in ["about", "who made you", "creator"]:
            return "I am a rule based chatbot created for learning Python concepts."

        return None

    def save_conversation(self) -> str:
        if not self.conversation_history:
            return "No conversation to save."

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_history_{timestamp}.txt"

        try:
            with open(filename, 'w', encoding='utf8') as f:
                f.write(f"Chat History {timestamp}\n")
                f.write("=" * 50 + "\n\n")

                if self.user_name:
                    f.write(f"User: {self.user_name}\n")

                f.write(f"ChatBot: {self.name}\n\n")
                f.write("Conversation:\n")
                f.write("=" * 50 + "\n")

                for entry in self.conversation_history:
                    time_str = entry["time"].strftime("%H:%M:%S")
                    f.write(f"[{time_str}] User: {entry['user']}\n")

            return f"Conversation saved to {filename}"

        except Exception as e:
            return f"Error saving conversation: {e}"

    def display_welcome(self):
        print("\n" + "=" * 60)
        print("WELCOME TO BASIC CHATBOT")
        print("=" * 60)
        print("\nType quit, exit, or bye to end the conversation")
        print("Type help to see what I can do")
        print("Type learn mode to teach me new responses")
        print("=" * 60)

    def chat_loop(self):
        self.display_welcome()
        print(f"\n{self.name}: Hello. I am {self.name}. What is your name?")

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
                    print(f"\n{self.name}: {self.get_response(user_input)}")

                    if self.conversation_history:
                        save = input(f"\n{self.name}: Would you like to save our conversation yes or no: ").lower()
                        if save in ["yes", "y"]:
                            print(f"{self.name}: {self.save_conversation()}")

                    print(f"\n{self.name}: Thanks for chatting. Come back anytime.")
                    break

                response = self.get_response(user_input)
                print(f"{self.name}: {response}")

                import time
                time.sleep(0.5)

            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye.")
                break
            except Exception as e:
                print(f"\n{self.name}: Error encountered: {e}")
                continue


def run_quick_demo():
    print("\n" + "=" * 60)
    print("QUICK DEMONSTRATION")
    print("=" * 60)

    demo_chat = [
        ("Hello!", None),
        ("Hi there! Nice to meet you!", None),
        ("What is your name?", None),
        ("I am ChatBot, your friendly chatbot!", None),
        ("My name is Alex", None),
        ("Nice to meet you, Alex! I will remember that.", None),
        ("How are you?", None),
        ("I am doing great, thank you. How about you?", None),
        ("I am good, thanks!", None),
        ("Tell me a joke", None),
        ("Why do not scientists trust atoms? Because they make up everything!", None),
        ("What time is it?", None),
        ("Let me check... It is [current time].", None),
        ("Bye!", None),
        ("Goodbye! Have a great day!", None)
    ]

    chatbot = BasicChatbot()

    for user_msg, _ in demo_chat:
        print(f"\nYou: {user_msg}")
        response = chatbot.get_response(user_msg)
        print(f"ChatBot: {response}")
        import time
        time.sleep(1)

    print("\n" + "=" * 60)
    print("Demo complete.")
    print("=" * 60)


def main():
    print("\n" + "=" * 60)
    print("BASIC RULE BASED CHATBOT")
    print("=" * 60)

    print("\nChoose an option:")
    print("1. Start Interactive Chat")
    print("2. Quick Demo")
    print("3. Exit")

    while True:
        try:
            choice = input("\nEnter your choice 1 to 3: ").strip()

            if choice == "1":
                chatbot = BasicChatbot()
                chatbot.chat_loop()
                break
            elif choice == "2":
                run_quick_demo()
                input("\nPress Enter to return to menu...")
                main()
                break
            elif choice == "3":
                print("\nGoodbye.")
                break
            else:
                print("Please enter 1 2 or 3.")

        except KeyboardInterrupt:
            print("\n\nGoodbye ")
            break
        except Exception as e:
            print(f"\nError: {e}")


def simple_chatbot():
    print("\n" + "=" * 40)
    print("SIMPLE CHATBOT")
    print("=" * 40)
    print("\nType bye to exit")
    print("=" * 40)

    responses = {
        "hello": ["Hi!", "Hello!", "Hey there!"],
        "hi": ["Hello!", "Hi!", "Hey!"],
        "how are you": ["I am fine, thanks!", "Doing well!", "Good, and you?"],
        "what's your name": ["I am ChatBot!", "Call me ChatBot!", "I am your friendly chatbot!"],
        "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
        "thank you": ["You are welcome!", "My pleasure!", "Happy to help!"]
    }

    print("\nChatBot: Hello. I am a simple chatbot.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "bye":
            print("ChatBot: Goodbye.")
            break

        response_found = False
        for pattern, response_list in responses.items():
            if pattern in user_input:
                print(f"ChatBot: {random.choice(response_list)}")
                response_found = True
                break

        if not response_found:
            print("ChatBot: I do not understand. Try saying hello or how are you or bye.")


if __name__ == "__main__":
    main()

