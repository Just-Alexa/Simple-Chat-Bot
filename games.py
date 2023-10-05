import random

def main():
    # Welcome the user to the game
    print("Welcome to Rock, Paper, Scissors. Good luck!")
    playing = True
    
    while playing:
        print()
        
    # Make a choice for the computer player
        choices = ("Rock", "Paper", "Scissors")
        computer_choice = random.choice(choices)

    
    # Get a choice from the user
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
        print()
    
    # Compare the user and computer choice
        print(f"The computer chooses {computer_choice}")
        print()
    
    # Print the result based on the choices
        if user_choice in choices:
            if computer_choice == user_choice:
                print(f"{computer_choice} and {user_choice}. It's a draw.")
            elif computer_choice == "Rock" and user_choice == "Scissors":
                print("Rock smashes Scissors. You lose!")
            elif computer_choice == "Scissors" and user_choice == "Paper":
                print("Scissors cut Paper. You lose!")
            elif computer_choice == "Paper" and user_choice == "Rock":
                print("Paper covers Rock. You lose!")
            elif computer_choice == "Scissors" and user_choice == "Rock":
                print("Rock smashes Scissors. You win!")
            elif computer_choice == "Paper" and user_choice == "Scissors":
                print("Scissors cut Paper. You win!")
            elif computer_choice == "Rock" and user_choice == "Paper":
                print("Paper covers Rock. You win!")
        else:
            print("You have to enter Rock, Paper, or Scissors.")
        play_again = input("play again? (y/n): ")
        if not play_again == "y":
            playing = False

        print("Thanks for playing, hope to see you next time. Bye!")

if __name__ == "__main__":
    main()