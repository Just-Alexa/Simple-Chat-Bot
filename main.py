import time
from todolist import main as todolist_main
from chat import main as chat_main
from games import main as games_main

time.sleep(1.4)
print("My name is ...")
time.sleep(1.4)

print("Sorry, I don't have a name yet. Would you like to name me? (Y/N)")
while True:
    user_response = input().lower()
    time.sleep(0.5)
    print()

    if user_response in ["y", "ya", "yeah", "yap", "ok", "yah", "sure", "yes"]:
        print("Great! What would you like to name me?")
        bot_name = input()
        time.sleep(1)
        print()
        break
    elif user_response in ["n", "nope", "nah", "no"]:
        print("That's okay, I'll just be called Chatty then.")
        bot_name = "Chatty"
        time.sleep(1)
        print()
        break
    else:
        print("I didn't understand that. Please try again. (Y/N)")
        time.sleep(0.5)
        print()
        continue

user_name = input(f"My name is {bot_name}, what's yours: ")
user_name = user_name if user_name else "Player 1"
print(f"Nice to meet you, {user_name}!")
time.sleep(1)
print()

print(f"So {user_name}, would you like to continue? (Y/N)")
while True:
    user_response = input().lower()
    time.sleep(0.5)
    print()

    if user_response in ["y", "yeah", "yap", "ok", "yah", "sure", "yes"]:
        print("What would you like to do today?")
        options = [
            "Organize my day",
            "Play Games",
            "Chat",
            "Exit",
        ]
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter the number of your choice (1-4): ")

        if choice == "1":
            print("You chose to organize your day.")
            todo_list = todolist_main()
            break
        elif choice == "2":
            print("You chose to play games.")
            games_main()
            break
        elif choice == "3":
            print("You chose to chat.")
            chat_main()
            break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")
    elif user_response in ["n", "nope", "nah", "no"]:
        print("Goodbye!")
        break
    else:
        print("I didn't understand that. Please try again. (Y/N)")
    print()
