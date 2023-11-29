from values import *
from colorama import Fore


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


def print_board():
    for column in array_of_board:
        for row in column:
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
            if row in array_of_X_pieces:
                if row < 10:
                    print(Fore.RED + f" {row}" + Fore.WHITE, end=" ")
                else:
                    print(Fore.RED + f"{row}" + Fore.WHITE, end=" ")
            elif row in array_of_O_pieces:
                if row < 10:
                    print(Fore.GREEN + f" {row}" + Fore.WHITE, end=" ")
                else:
                    print(Fore.GREEN + f"{row}" + Fore.WHITE, end=" ")
            else:
                if not row == "|" and row < 10:
                    print(f" {row}", end=" ")
                else:
                    print(row, end=" ")
        print("\n", end="")
    print(Fore.RESET, end="")
    print(end="\n")


def move_piece(self, name):
    is_choosing = True
    while is_choosing:
        moving_piece = int(input("Select a piece you want to move: "))
        column_index_of_moving_piece = 0
        row_index_of_moving_piece = 0
        for index, value in enumerate(array_of_board_helping):
            if moving_piece in array_of_board_helping[index]:
                column_index_of_moving_piece = index
                tempo_index = array_of_board_helping[index]
                row_index_of_moving_piece = tempo_index.index(moving_piece)
        if self:
            if array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] == "X":
                possible_moves = []
                if 0 < column_index_of_moving_piece < 7:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2])

                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2])

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2])

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2])

                elif column_index_of_moving_piece == 0:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2])

                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2])

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2])

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2])

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
                                            array_of_board[final_column][final_row] = "X"
                                            array_of_X_pieces.clear()
                                            possible_moves.clear()
                                            is_choosing_move = False
                                            is_choosing = False

        else:
            if array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] == "O":
                possible_moves = []
                if 0 < column_index_of_moving_piece < 7:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2])

                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2])

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2])

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2])

                elif column_index_of_moving_piece == 7:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2])

                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2])

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2])

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves.append(array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2])

                elif column_index_of_moving_piece == 0:
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
                                            array_of_board[final_column][final_row] = "O"
                                            array_of_O_pieces.clear()
                                            possible_moves.clear()
                                            is_choosing_move = False
                                            is_choosing = False
