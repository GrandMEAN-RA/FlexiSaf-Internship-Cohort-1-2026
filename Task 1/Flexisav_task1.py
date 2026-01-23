
import random

# 1. Define the possible choices
choices = ["rock", "paper", "scissors"]

while True:
    # 2. Get the user's choice
    print("It's your turn!")
    print("Choose rock, paper, or scissors. You can type r for rock; p for paper; s for scissors: ")
    user_choice = input("Make your choice or press e to exit the game.").lower()
    if user_choice in ["r","rock"]:
        user_choice = "rock"
    elif user_choice in ["p","paper"]:
        user_choice = "paper"
    elif user_choice in ["s","scissors"]:
        user_choice = "scissors"
    elif user_choice in ["e","exit"]:
        print("Exiting the game >>>")
        print("Game ended and closed!")
        break

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
    else:
        # 3. Generate a random choice for the computer
        print("it's now computer's turn")
        computer_choice = random.choice(choices)

        # 4. Determine the winner
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("Applauds! You win!")
        else:
            print("Oops! Computer wins!")

    response = input("Do you want to play again? >>>").lower()
    if response in ["y","yes"]:
        continue
    else:
        print("Exiting the game >>>")
        print("Game ended and closed!")
        break

