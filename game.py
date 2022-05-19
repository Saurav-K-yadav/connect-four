import numpy as np
import sys
import pygame  # For the GUI
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


def win(board, piece):  # check if the player is winning
    # checking horizontolly
    for cols in range(col_count - 3):  # last three can't make horizontal pattern
        for rows in range(row_count):
            if (
                (board[rows][cols] == piece)
                and (board[rows][cols + 1] == piece)
                and (board[rows][cols + 2] == piece)
                and (board[rows][cols + 3] == piece)
            ):
                return True

    # Checking Vertically
    for cols in range(col_count):
        for rows in range(row_count - 3):  # Top ones can't make the pattern
            if (
                (board[rows][cols] == piece)
                and (board[rows + 1][cols] == piece)
                and (board[rows + 2][cols] == piece)
                and (board[rows + 3][cols] == piece)
            ):
                return True

    # For Diagnols
    # For going upwards
    for cols in range(col_count - 3):  # right ones can't make the pattern
        for rows in range(row_count - 3):  # Top ones can't make the pattern
            if (
                (board[rows][cols] == piece)
                and (board[rows + 1][cols + 1] == piece)
                and (board[rows + 2][cols + 2] == piece)
                and (board[rows + 3][cols + 3] == piece)
            ):
                return True
    # For diagnolly downwards
    for cols in range(col_count - 3):  # right ones can't make the pattern
        for rows in range(3, row_count):  # bottom ones can't make the pattern
            if (
                (board[rows][cols] == piece)
                and (board[rows - 1][cols + 1] == piece)
                and (board[rows - 2][cols + 2] == piece)
                and (board[rows - 3][cols + 3] == piece)
            ):
                return True


def draw_board(board):  # GUI for the board
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(
                screen,
                (0, 0, 255),
                (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE),
            )  # draw blue squares
            # surface,color,position,dimension
            pygame.draw.circle(
                screen,
                (255,255,255),
                (
                    int(c * SQUARESIZE + SQUARESIZE / 2),
                    int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2),
                ),
                RADIUS,
            )  # Draw the circle
            # surface,color,position,radius
            # BLACK FOR EMPTY

    for c in range(col_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen,
                    (255, 255, 0),
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        height - int(r * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )  # Draw the circle
                # surface,color,position,radius
                # value is subtracted from height as 0,0 is left top but we need to fill from bottom
                # Player 1 Yellow

            elif board[r][c] == 2:
                pygame.draw.circle(
                    screen,
                    (255, 0, 0),
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        height - int(r * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )  # Draw the circle
                # surface,color,position,radius
                # value is subtracted from height as 0,0 is left top but we need to fill from bottom
                # Player 2 red

    pygame.display.update()  # To update the screen


if __name__ == "__main__":

    board = board()  # A 6*7 matrix with all zeros
    game_over = False
    turn = 0  # player 1 goes first

    pygame.init()  # initializing the pygame
    SQUARESIZE = 100  # 1 square sixe is 100 pixel
    RADIUS = int(SQUARESIZE / 2 - 5)  # Radius of the inner circle
    width = col_count * SQUARESIZE
    height = (row_count + 1) * SQUARESIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)  # The dimensions of the game area
    draw_board(board)
    pygame.display.update()  # To update the screen
    my_font=pygame.font.SysFont("monospace",45)#Font of the final message

    while not game_over:
        for event in pygame.event.get():
            # Whenever a event like key press/mouse movement occurs
            if event.type == pygame.QUIT:  # If the player clicks upper red X bar
                sys.exit()

            if event.type == pygame.MOUSEMOTION:  # Whenever the mouse moves
                # For the upper space
                pygame.draw.rect(screen, (0,0,0), (0, 0, width, SQUARESIZE))
                # masks previous colour
                posx = event.pos[0]
                if turn == 0:  # for player 1
                    pygame.draw.circle(
                        screen, (255, 255, 0), (posx, int(SQUARESIZE / 2)), RADIUS
                    )
                else:  # for player 2
                    pygame.draw.circle(
                        screen, (255, 0, 0), (posx, int(SQUARESIZE / 2)), RADIUS
                    )
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # if   mouse is clicked
                pygame.draw.rect(screen,(0,0,0),(0,0,width,SQUARESIZE))#Masks previous coloured circle

                # player 1's turn
                if turn == 0:
                    # col_move = int(input(" Player 1's turn "))  # User enters column values
                    posx = event.pos[0]  # position of x-axis of mouse click
                    col_move = int(math.floor(posx / SQUARESIZE))
                    if can_put(board, col_move):
                        row = next_top_row(board, col_move)
                        put_piece(board, row, col_move, 1)  # player 1's piece is 1
                    print_board(board)
                    draw_board(board)

                    if win(board, 1):
                        label=my_font.render("!!! Player 1 Wins !!!",1,(255,255,0))
                        screen.blit(label,(40,10))
                        # The winning message
                        game_over = True  # The game is over

                else:  # Player 2's turn
                    # col_move = int(input(" Player 2's turn "))
                    posx = event.pos[0]  # position of x-axis of mouse click
                    col_move = int(math.floor(posx / SQUARESIZE))
                    if can_put(board, col_move):
                        row = next_top_row(board, col_move)
                        put_piece(board, row, col_move, 2)  # player 2's piece is 2
                    print_board(board)

                    if win(board, 2):
                        label=my_font.render("!!! Player 2 Wins !!!",1,(255,0,0))
                        screen.blit(label,(40,10))
                        # The winning message
                        
                        game_over = True  # The game is over

                draw_board(board)
                
                turn += 1
                turn = turn % 2  # Turn we either be 0 or 1
                if game_over:
                    pygame.time.wait(5000)#Wait before closing the window after game is over
