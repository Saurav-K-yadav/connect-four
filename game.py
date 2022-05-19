import numpy as np
import math

row_count = 6  # total no of rows
col_count = 7  # total number of columns


def board():
    board = np.zeros((row_count, col_count))  # Make a matrix of 6*7 with all zeros
    return board


def put_piece(board, row, col, piece):  # Puts a piece in given cell
    board[row][col] = piece
    return


def can_put(board, col):  # if the column is completely filled or not
    if board[row_count - 1][col] == 0:
        return 1
    else:
        print("Can't put any more pieces in this column")
        return 0


def next_top_row(board, col):  # get empty row in given column
    for i in range(row_count):
        if board[i][col] == 0:
            return i


def print_board(board):  # To print the game board
    print(np.flip(board, 0))  # flip the board along 0


board = board()  # A 6*7 matrix with all zeros
game_over = False
turn = 0  # player 1 goes first

while not game_over:
    # player 1's turn
    if turn == 0:
        col_move = int(input(" Player 1's turn "))  # User enters column values
        if can_put(board, col_move):
            row = next_top_row(board, col_move)
            put_piece(board, row, col_move, 1)  # player 1's piece is 1

    else:  # Player 2's turn
        col_move = int(input(" Player 2's turn "))
        if can_put(board, col_move):
            row = next_top_row(board, col_move)
            put_piece(board, row, col_move, 2)  # player 2's piece is 2

    print_board(board)
    turn += 1
    turn = turn % 2  # Turn we either be 0 or 1
