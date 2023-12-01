import methods
from colorama import Fore
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


def create_helping_board():
    counter = 1
    for column in range(8):
        row_counter = 0
        for row in range(17):
            if row_counter % 2 == 1:
                if counter < 10:
                    array_of_board_helping[column][row] = counter
                else:
                    array_of_board_helping[column][row] = counter
                row_counter += 1
                counter += 1
                continue
            array_of_board_helping[column][row] = "|"
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

    array_of_board[6][3] = "X"
    array_of_board[1][1] = "O"


def print_board():
    for column in array_of_board:
        for row in column:
            index_of_column = array_of_board.index(column)
            index_of_row = column.index(row)
            if (O_queens[index_of_column][index_of_row] == 1 or
                    X_queens[index_of_column][index_of_row] == 1):
                print(Fore.WHITE + row + Fore.RESET, end=" ")
                continue
            print(row, end=" ")
        print("\n", end="")
    print(end="\n")


def print_helping_board():
    copy_of_array_of_board = array_of_board.copy()
    counter = 1
    for column in copy_of_array_of_board:
        for row in column:
            if row == "X":
                array_of_X_pieces.append(counter)
                counter += 1
            elif row == "O":
                array_of_O_pieces.append(counter)
                counter += 1
            elif row == " ":
                counter += 1
    print(Fore.WHITE, end="")

    for column in array_of_board_helping:
        for row in column:
            index_of_column = array_of_board_helping.index(column)
            index_of_row = column.index(row)
            if row in array_of_X_pieces:
                methods.print_pieces(index_of_column, index_of_row, row, "X")
            elif row in array_of_O_pieces:
                methods.print_pieces(index_of_column, index_of_row, row, "O")
            else:
                if not row == "|" and row < 10:
                    print(Fore.WHITE + f" {row}" + Fore.WHITE, end=" ")
                else:
                    print(Fore.WHITE + f"{row}" + Fore.WHITE, end=" ")
        print("\n", end="")
    print(Fore.RESET, end="")
    print(end="\n")

#Rozdeleni metody move_piece
def move_piece(self, name):
    is_choosing = True
    while is_choosing:
        moving_piece = int(input("Select a piece you want to move: "))
        column_index_of_moving_piece = 0
        row_index_of_moving_piece = 0
        queen_playing = False
        for index, value in enumerate(array_of_board_helping):
            if moving_piece in array_of_board_helping[index]:
                column_index_of_moving_piece = index
                tempo_index = array_of_board_helping[index]
                row_index_of_moving_piece = tempo_index.index(moving_piece)
        if self:
            moving_indicator = column_index_of_moving_piece + 1
            indicator_of_moving_element = "X"
        else:
            moving_indicator = column_index_of_moving_piece - 1
            indicator_of_moving_element = "O"

        if ((array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] == "X" and self)
                or (array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] == "O" and not self)):
            possible_moves = []
            if (X_queens[column_index_of_moving_piece][row_index_of_moving_piece] == 1 or
                    O_queens[column_index_of_moving_piece][row_index_of_moving_piece] == 1):
                possible_moves = methods.Queen(column_index_of_moving_piece, row_index_of_moving_piece).queen_movement()
                queen_playing = True
            else:
                if 0 <= column_index_of_moving_piece < 7:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[moving_indicator][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(
                                array_of_board_helping[moving_indicator][row_index_of_moving_piece + 2]
                            )

                        if array_of_board[moving_indicator][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(
                                array_of_board_helping[moving_indicator][row_index_of_moving_piece - 2]
                            )

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[moving_indicator][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(
                                array_of_board_helping[moving_indicator][row_index_of_moving_piece + 2]
                            )

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[moving_indicator][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(
                                array_of_board_helping[moving_indicator][row_index_of_moving_piece - 2]
                            )

                elif column_index_of_moving_piece == 7:
                    print(f"Player {name} has gained a Queen.")

            if not possible_moves:
                print(f"There can not be done any moves to {moving_piece}")
            else:
                print(f"Possible moves in {moving_piece} are: {' '.join(map(str, possible_moves))}")
                is_choosing_move = True
                while is_choosing_move:
                    final_move = int(input("Move: "))
                    for num in possible_moves:
                        if final_move == num:
                            array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] = " "
                            for column in array_of_board_helping:
                                for row in column:
                                    if final_move == row:
                                        final_column = array_of_board_helping.index(column)
                                        final_row = column.index(row)
                                        if indicator_of_moving_element == "X":
                                            if queen_playing:
                                                X_queens[column_index_of_moving_piece][row_index_of_moving_piece] = "|"
                                                X_queens[final_column][final_row] = 1
                                            array_of_board[final_column][final_row] = "X"
                                            array_of_X_pieces.clear()
                                        elif indicator_of_moving_element == "O":
                                            if queen_playing:
                                                O_queens[column_index_of_moving_piece][row_index_of_moving_piece] = "|"
                                                O_queens[final_column][final_row] = 1
                                            array_of_board[final_column][final_row] = "O"
                                            array_of_O_pieces.clear()
                                        possible_moves.clear()
                                        methods.Queen(final_column, final_row).has_queen(self, name)
                                        is_choosing_move = False
                                        is_choosing = False
