"""
CodSoft AI Internship - Task 2
Tic-Tac-Toe AI using Minimax Algorithm
Author: Bandi Vijaya Siva Sai Naga Jyothi
"""

import math

# ─────────────────────────────────────────────
# Board Setup
# Board is a list of 9 cells: index 0-8
# ' ' = empty, 'X' = human, 'O' = AI
# ─────────────────────────────────────────────

def create_board():
    return [' '] * 9


def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def print_position_guide():
    print("\n  Position guide:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")


# ─────────────────────────────────────────────
# Game Logic
# ─────────────────────────────────────────────

WIN_COMBINATIONS = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],  # left column
    [1, 4, 7],  # middle column
    [2, 5, 8],  # right column
    [0, 4, 8],  # diagonal
    [2, 4, 6],  # anti-diagonal
]


def check_winner(board, player):
    for combo in WIN_COMBINATIONS:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_board_full(board):
    return ' ' not in board


def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']


# ─────────────────────────────────────────────
# Minimax Algorithm
# AI = 'O' (maximizer), Human = 'X' (minimizer)
# ─────────────────────────────────────────────

def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# ─────────────────────────────────────────────
# Human Input
# ─────────────────────────────────────────────

def get_human_move(board):
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That cell is already taken. Try another.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


# ─────────────────────────────────────────────
# Main Game Loop
# ─────────────────────────────────────────────

def play_game():
    print("=" * 45)
    print("     Tic-Tac-Toe AI — CodSoft Task 2")
    print("     You = X  |  AI = O")
    print("=" * 45)
    print_position_guide()

    board = create_board()

    choice = input("Do you want to go first? (y/n): ").strip().lower()
    human_turn = choice == 'y'

    while True:
        print_board(board)

        if human_turn:
            print("Your turn (X):")
            move = get_human_move(board)
            board[move] = 'X'
            if check_winner(board, 'X'):
                print_board(board)
                print("Congratulations! You won! (That's rare!)")
                break
        else:
            print("AI is thinking...")
            move = get_best_move(board)
            board[move] = 'O'
            print(f"AI placed O at position {move + 1}")
            if check_winner(board, 'O'):
                print_board(board)
                print("AI wins! Better luck next time.")
                break

        if is_board_full(board):
            print_board(board)
            print("It's a draw! Well played.")
            break

        human_turn = not human_turn

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    play_game()