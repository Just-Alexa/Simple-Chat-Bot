import time

print("Hi there! I'm your chatbot.")
time.sleep(1)  # Delay for 1 second
print("My name is ...")
time.sleep(1)  # Delay for 1 second

print("Sorry, I don't have a name yet. Would you like to name me? (Y/N)")
while True:
    bot_choice = input().lower()
    time.sleep(0.5)  # Delay for 0.5 seconds
    print()

    if bot_choice in ["y", "yeah", "yap", "ok", "yah", "sure", "yes"]:
        print("Great! What would you like to name me?")
        bot_name = input()
        time.sleep(1)  # Delay for 1 second
        print()
        break
    elif bot_choice in ["n", "nope", "nah", "no"]:
        print("That's okay, I'll just be called Chatty then.")
        bot_name = "Chatty"
        time.sleep(1)  # Delay for 1 second
        print()
        break
    else:
        print("I didn't understand that. Please try again. (Y/N)")
        time.sleep(0.5)  # Delay for 0.5 seconds
        print()
        continue

user_name = input(f"My name is {bot_name}, what's yours: ")
user_name = user_name if user_name else "Player 1"
print(f"Nice to meet you, {user_name}!")
time.sleep(1)  # Delay for 1 second
print()

print(f"So {user_name}, would you like to continue? (Y/N)")
while True:
    bot_choice = input().lower()
    time.sleep(0.5)  # Delay for 0.5 seconds
    print()

    if bot_choice in ["y", "yeah", "yap", "ok", "yah", "sure", "yes"]:
        print("What would you like to do today?")
        options = [
            "Organize my day (todo list)",
            "Play Games",
            "Chat",
            "Exit",
        ]
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter the number of your choice (1-4): ")

        if choice == "1":
            # Add code for the to-do list functionality here
            print("You chose to organize your day.")
            # Implement the to-do list functionality or call a function here
            break
        elif choice == "2":
            # Add code for playing games here
            print("You chose to play games.")
            # Implement game-related functionality or call a function here
            break
        elif choice == "3":
            # Add code for chatting here
            print("You chose to chat.")
            # Implement chat-related functionality or call a function here
            break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")
    elif bot_choice in ["n", "nope", "nah", "no"]:
        print("Goodbye!")
        break
    else:
        print("I didn't understand that. Please try again. (Y/N)")
