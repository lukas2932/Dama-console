from values import *


def create_board():
    for column in range(8):
        row_counter = 0
        for row in range(17):
            if row_counter % 2 == 1:
                array_of_board[column][row] = " "
                row_counter += 1
                continue
            array_of_board[column][row] = "|"

            row_counter += 1


def create_figures():
    placement_counter = 0
    reverse = False
    for column in range(3):
        for row in range(16):
            if reverse:
                if placement_counter % 4 == 3:
                    array_of_board[column][row] = "X"
                if placement_counter % 4 == 1:
                    array_of_board[column - column - column - 1][row] = "O"
            else:
                if placement_counter % 4 == 1:
                    array_of_board[column][row] = "X"
                if placement_counter % 4 == 3:
                    array_of_board[column - column - column - 1][row] = "O"

            placement_counter += 1
        if reverse:
            reverse = False
        else:
            reverse = True


def print_board():
    for column in array_of_board:
        for row in column:
            print(row, end=" ")
        print("\n", end="")
