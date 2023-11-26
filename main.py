import board
from board import *


def game():
    board.create_board()
    board.create_figures()
    board.print_board()


if __name__ == '__main__':
    game()
