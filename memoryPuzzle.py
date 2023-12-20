import random
import time

#initialising cards as symbols 
def initialize_board():
    symbols = ["A", "B", "C", "D", "E", "F", "G", "H"] * 2
    random.shuffle(symbols)
    board = [symbols[i:i + 4] for i in range(0, 8, 4)]
    return board

def display_board(board, revealed):
    for i in range(4):
        for j in range(4):
            if revealed[i][j]:
                print(board[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

#getting user input 
def get_user_input():
    row = int(input("Enter row (0 to 3): "))
    col = int(input("Enter column (0 to 3): "))
    return row, col


#game funciton
def play_memory_puzzle():
    board = initialize_board()
    revealed = [[False] * 4 for _ in range(4)]
    matched_pairs = 0
    moves = 0
    time_limit = 60 
    start_time = time.time()

    while matched_pairs < 8 and time.time() - start_time < time_limit:
        print("\nMoves:", moves)
        display_board(board, revealed)

        print("\nTime left:", max(0, int(time_limit - (time.time() - start_time))), "seconds")

        row1, col1 = get_user_input()
        while revealed[row1][col1]:
            print("Card already revealed. Try again.")
            row1, col1 = get_user_input()

        revealed[row1][col1] = True
        display_board(board, revealed)

        row2, col2 = get_user_input()
        while revealed[row2][col2] or (row1 == row2 and col1 == col2):
            print("Invalid selection. Try again.")
            row2, col2 = get_user_input()

        revealed[row2][col2] = True
        display_board(board, revealed)

        moves += 1

        if board[row1][col1] == board[row2][col2]:
            print("Match found!")
            matched_pairs += 1
        else:
            print("No match. Try again.")
            revealed[row1][col1] = revealed[row2][col2] = False

    if matched_pairs == 8:
        print("Congratulations! You matched all pairs.")
    else:
        print("Time's up! Game over.")


#game starts
play_memory_puzzle()
