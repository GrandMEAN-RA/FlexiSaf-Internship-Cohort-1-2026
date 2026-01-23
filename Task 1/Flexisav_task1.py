
import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

player = input("Welcome to the game of rock, paper and scissors. \nPlease input your preferred username. >>>")
print(f"Welcome {player}! I hope you have a nice time playing")

while True:
    # Get the user's choice
    print(f"It's your turn! {player}")
    print("Choose rock, paper, or scissors. You can type r for rock; p for paper; s for scissors: ")
    user_choice = input("Make your choice or press e to exit the game.").lower()

    # Validate user input
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
    else:
        print("Invalid choice! Try again: Please choose rock, paper, or scissors.")
        continue
    
    print(f"Your choice: {user_choice}")
    
    # Generate a random choice for the computer
    print("it's now computer's turn")
    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
        player_score += 0
        computer_score += 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print(f"Applauds! {player}, you win!")
        player_score += 5
        computer_score += 0
    else:
        print(f"Oops {player}! Computer wins!")
        player_score += 0
        computer_score += 5

    print(f"Your current score: {player_score} \ncomputer's current score: {computer_score}")
    if player_score > computer_score:
        margin = player_score - computer_score
        print(f"You are leading by {margin} points")
    elif  player_score < computer_score:
        margin = computer_score - player_score
        print(f"Computer is leading by {margin} points")
    else:
        margin = 0
        print("No winner")
    
    response = input("Do you want to play again? >>>").lower()
    if response in ["y","yes"]:
        continue
    else:
        print("Exiting the game >>>")
        print("Game ended and closed!")
        break

