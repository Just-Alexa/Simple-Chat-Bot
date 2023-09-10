import random

# Define lists of greetings, questions, and responses
greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
questions = ["How are you today?", "What's new in your world?", "Anything exciting happening?"]
responses = [
    "That's interesting.",
    "Tell me more about that.",
    "I see. How do you feel about it?",
    "Interesting! How did that make you feel?",
]

# Function to generate a random response
def get_random_response(options):
    return random.choice(options)
    
# Function to handle user input and generate responses
def chat(bot_name):
    print(f"{bot_name}: " + get_random_response(greetings))
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print(f"{bot_name}: Goodbye! Have a great day.")
            break
        elif 'how are you' in user_input.lower():
            print(f"{bot_name}: I'm just a computer program, so I don't have feelings, but I'm here to chat with you!")
        else:
            response = get_random_response(responses)
            print(f"{bot_name}: " + response)

def main():
    bot_name = "Chatty"  # Specify the chatbot's name here
    print(f"{bot_name}: Hello! I'm a {bot_name}. You can start a conversation with me. Type 'exit' to end the chat.")
    chat(bot_name)

if __name__ == "__main__":
    main()