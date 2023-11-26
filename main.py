import board
from board import *


def game():
    board.create_board()
    board.create_figures()

    for column in array_of_board:
        for row in column:
            print(row, end=" ")
        print("\n", end="")


if __name__ == '__main__':
    game()
