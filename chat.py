import random

class ChatBot:
    def __init__(self):
        self.responses = {
            "hello": ["wats up!"],
            "hi": ["wats up!"],
            "i'm doing well": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "i'm great": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "i'm good": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "good": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "cool": ["That's groovy!"],
            "nice": ["I know right!"],
            "me too": ["great!"],
            "love you": ["Well I don't; I just met you!", "love you too"],
            "helpful": ["It's thanks to my creator!"],
            "fine": ["That's good to hear!", "Awesome!", "Glad to hear it!"],
            "not much": ["Tell me about it!", "Same here!"],
            "nothing much": ["Really? I'm doing a lot!", "Same here!"],
            "what are you doing": ["Waiting on your command!", "I'm just hanging out.", "I'm here to chat with you!"],
            "what's up": ["Not much! What's up with you", "The sky!"],
            "wats up": ["Not much! What's up with you", "The sky!"],
            "how's your day going": ["Great! And how's your day going?", "Not too bad.", "Just another day in paradise."],
            "how are you": ["I'm doing well, thanks!", "Although I am a program, I feel great!"],
            "tell me a joke": ["Why did the computer catch a cold? It had too many windows open!", "Here's one: What do you call a computer that sings? A-Dell!"],
            "chatting": ["I love chatting with you!", "I'm glad we're chatting now!"],
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for keyword, responses in self.responses.items():
            if keyword in user_input:
                return random.choice(responses)
        return "I'm not sure how to respond to that."

    def handle_exit(self):
        print("ChatBot: Catch you later aligator.")

    def chat_with_user(self):
        print("ChatBot: Hi there!")
        while True:
            user_input = input("You: ").lower()
            if user_input in ['exit', 'quit', 'bye', 'goodbye']:
                self.handle_exit()
                break
            response = self.get_response(user_input)
            print(f"ChatBot: {response}")

def main():
    print("Welcome to the ChatBot!")
    chatbot = ChatBot()
    chatbot.chat_with_user()

if __name__ == "__main__":
    main()