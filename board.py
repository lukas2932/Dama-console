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
    for column in array_of_board_helping:
        for row in column:
            print(row, end=" ")
        print("\n", end="")

    print(end="\n")


def move_piece(self):
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
                possible_moves = ""
                if 0 < column_index_of_moving_piece < 7:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2]} "

                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2]} "

                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2]} "

                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2]} "

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2]} "

                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2]} "

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2]} "

                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2]} "

                elif column_index_of_moving_piece == 0:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2]} "

                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2]} "

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece + 2]} "

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece + 1][row_index_of_moving_piece - 2]} "

                elif column_index_of_moving_piece == 7:
                    if 1 < row_index_of_moving_piece < 15:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2]} "

                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2]} "

                    elif row_index_of_moving_piece == 1:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece + 2]} "

                    elif row_index_of_moving_piece == 15:
                        if array_of_board[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2] == " ":
                            possible_moves += f"{array_of_board_helping[column_index_of_moving_piece - 1][row_index_of_moving_piece - 2]} "

                if not possible_moves:
                    print(f"There can not be done any moves to {moving_piece}")
                else:
                    print(f"Possible moves in {moving_piece} are: {possible_moves}")
                    is_choosing_move = True
                    while is_choosing_move:
                        final_move = input("Move: ")
                        if final_move in possible_moves:
                            array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] = " "
                            final_column = 0
                            final_row = 0
                            for column in array_of_board_helping:
                                for row in column:
                                    if final_move == str(row):
                                        final_column = array_of_board_helping.index(column)
                                        final_row = column.index(row)

                            array_of_board[final_column][final_row] = "X"
                            is_choosing_move = False
                            is_choosing = False
        else:
            is_choosing = False
            pass
