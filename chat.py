import random

class ChatBot:
    def __init__(self):
        self.responses = {
            "hello": ["Hello!", "Hi there!", "Hey!", "wats up!" "Greetings!"],
            "I'm doing well": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "I'm great": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "I'm good": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "good": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "fine": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "what are you doing": ["Waiting on your command!", "I'm just hanging out.", "I'm here to chat with you!"],
            "what's up": ["Not much!", "The sky!"],
            "how's your day going": ["Great!", "Not too bad.", "Just another day in paradise."],
            "how are you": ["I'm doing well, thanks!", "I'm just a computer program, but I'm here to chat with you!"],
            "tell me a joke": ["Why did the computer catch a cold? It had too many windows open!", "Here's one: What do you call a computer that sings? A-Dell!"],
            "goodbye": ["Goodbye!", "Have a great day!"],
            "bye": ["Catch you later, aligator!"],
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for keyword, responses in self.responses.items():
            if keyword in user_input:
                return random.choice(responses)
        return "I'm not sure how to respond to that."

    def chat_with_user(self):
        print("ChatBot: Hello! How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                print("ChatBot: Goodbye! Have a great day.")
                break
            response = self.get_response(user_input)
            print(f"ChatBot: {response}")

def main():
    print("Welcome to the ChatBot!")
    chatbot = ChatBot()
    chatbot.chat_with_user()

if __name__ == "__main__":
    main()