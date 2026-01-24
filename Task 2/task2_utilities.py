

import random

# -----------------------------
# Define the game board
# -----------------------------
def create_board():
    return [" "] * 9


def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()


# -----------------------------
# Check if a player has won
# -----------------------------
def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


# -----------------------------
# Check if the game is a tie
# -----------------------------
def check_tie(board):
    return " " not in board


# -----------------------------
# AI Memory (Learning)
# -----------------------------
ai_memory = {}  # board_state -> score


def get_board_state(board):
    return "".join(board)


def ai_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    best_score = -float("inf")
    best_move = random.choice(available_moves)

    for move in available_moves:
        board[move] = "O"
        state = get_board_state(board)
        score = ai_memory.get(state, 0)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def update_memory(state, reward):
    ai_memory[state] = ai_memory.get(state, 0) + reward


    
