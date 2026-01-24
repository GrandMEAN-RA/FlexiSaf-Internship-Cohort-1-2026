
from task2_utilities import create_board, print_board, check_winner, check_tie
from task2_utilities import get_board_state, ai_move, update_memory

# -----------------------------
# Main game loop
# -----------------------------
def main_game():
    
    print("TIC-TAC-TOE: GAME SETUP")
    mode = input("Select game mode: 1 AI mode, 2 for two players >>> ")

    if mode.isnumeric():
        if int(mode) == 2:
            game_mode = "two players"
            user1 = input("User 1: input your preferred username >>> ")
            user2 = input ("User 2: input your preferred username >>> ")
        elif int(mode) == 1:
            game_mode = "AI mode"
            user = input("Input your preferred username >>> ")
        else:
            game_mode = "AI mode"
            print("Invalid response. Sngle player mode activated")
            user = input("Input your preferred username >>> ")
    else:
        game_mode = "AI mode"
        print("Invalid response. AI mode mode activated")
        user = input("Input your preferred username >>> ")
    
    print(f"Tic-Tac-Toe: {user} (X) vs AI (O)" if game_mode == "AI mode" else f"Tic-Tac-Toe: {user1} (X) vs {user2} (O)")

    while True:
        board = create_board()
        print_board(board)
    
        while True:
            # Player move
            while True:
                move = input(f"{user1}, choose position (1-9): >>> ") if game_mode == "two players" else input(f"{user}, choose position (1-9): >>>")
                if not move.isnumeric():
                    print("Invalid move! Please try again")
                    continue
                
                move = int(move) - 1
                if move < 0 or move > 8:
                    print("Move must be between 1 and 9. Please try again")
                    continue
                if board[move] != " ":
                    print("Position already taken!")
                    continue
                break

            if board[move] != " ":
                print("Invalid move!")
                continue

            board[move] = "X"
            print_board(board)
            
            if check_winner(board, "X"):
                print_board(board)
                print(f"{user}, you win!") if game_mode == "AI mode" else print(f"{user1}, you win!")
                update_memory(get_board_state(board), -1)
                break

            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break
                
            if game_mode == "AI mode":
                # AI move
                ai_choice = ai_move(board)
                board[ai_choice] = "O"
                print_board(board)

                if check_winner(board, "O"):
                    print_board(board)
                    print("AI wins!")
                    update_memory(get_board_state(board), 1)
                    break

                if check_tie(board):
                    print_board(board)
                    print("It's a tie!")
                    break

            if game_mode == "two players":
                # Player-2 move
                while True:
                    move = input(f"{user2}, choose position (1-9): >>> ")
                    if not move.isnumeric():
                        print("Invalid move! Try again.")
                        continue

                    move = int(move) - 1

                    if move < 0 or move > 8:
                        print("Move must be between 1 and 9.")
                        continue

                    if board[move] != " ":
                        print("Position already taken!")
                        continue
                    break

                board[move] = "O"
                print_board(board)

                if check_winner(board, "O"):
                    print_board(board)
                    print(f"{user2}, you win!")
                    update_memory(get_board_state(board), -1)
                    break

                if check_tie(board):
                    print_board(board)
                    print("It's a tie!")
                    break

        response = input("Play again? Y or N >>> ")
        if response.lower() in ["y", "yes"]:
            continue
        else:
            print("Game closed!")
            break
      
# -----------------------------
# Call the main game loop
# -----------------------------
if __name__ == "__main__":
    main_game()
