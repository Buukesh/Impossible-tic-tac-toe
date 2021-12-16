import sys
import math
import random

board = {0: ' ', 1: ' ', 2: ' ',
         3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' '}


def print_grid(blank):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")


def user_input(player_num, side, board):
    # Ask for user input 1-9
    user_num = int(
        input("Player #{} Enter number from 1-9.\n".format(player_num)))  # need to add check if user adds number outside of expected boundary
    # only place letter if spot is clear
    if(board[user_num - 1] == ' '):
        board[user_num - 1] = side
    # tell user to choose another spot
    else:
        while(board[user_num - 1] != ' '):
            print("That space is already taken.")
            user_num = int(
                input("Player #{} Enter number from 1-9.\n".format(player_num)))

        board[user_num - 1] = side


def play_game(board):
    while True:
        user_input(1, "X", board)  # asks p1 input
        print_grid(board)  # prints grid
        check = check_win(board)  # check returns X, O, 0 or None
        display_winner(check)   # if potential winner print winner
        best_turn(board)  # swap to unbeatable CPU input
        # user_input(2, "O", board)  #swap to p2 input
        print_grid(board)
        check = check_win(board)
        display_winner(check)


def check_win(board):

    winner = None
    for i in range(0, 9, 3):  # checks for horizontal row wins
        if board[i] != ' ' and board[i + 1] != ' ' and board[i + 2] != ' ' and board[i] == board[i + 1] == board[i + 2]:
            winner = board[i]
            return winner

    for i in range(0, 3):  # checks for vertical column wins
        if board[i] != ' ' and board[i + 3] != ' ' and board[i + 6] != ' ' and board[i] == board[i + 3] == board[i + 6]:
            winner = board[i]
            return winner

    # checks for diagonal top left win
    if board[0] == board[4] == board[8] and board[0] != ' ' and board[4] != ' ' and board[8] != ' ':
        winner = board[4]
        return winner

    # checks for diagonal top right win
    if board[2] == board[4] == board[6] and board[2] != ' ' and board[4] != ' ' and board[6] != ' ':
        winner = board[4]
        return winner

    free_spots = 9
    for i, possible_values in board.items():  # checks for tie
        if board[i] == 'X' or board[i] == 'O':
            free_spots -= 1
            if free_spots == 0:  # if there are no freespots, tie
                return 0

# displays winner based on letter check recieved


def display_winner(check):
    if check == 'X' or check == 'O':
        print(f"{check} wins!")
        sys.exit(0)
    elif check == 0:
        print("Tie!")
        sys.exit(0)

# CPU chooses best move possible


def best_turn(board):
    best_score = -math.inf
    for i in range(0, 9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if (score > best_score):
                best_score = score
                move = i
    board[move] = 'O'


def minimax(board, depth, is_maximizing):
    result = check_win(board)
    scores = {0: 0, 'X': -10, 'O': 10}
    if result != None:
        return scores[result]
    if is_maximizing == True:
        best_score = -math.inf
        for i in range(0, 9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(0, 9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


play_game(board)
