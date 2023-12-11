import queen
import corrections_and_detections
from colorama import Fore
from arrays import *


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
    x_pieces_counter = 0
    o_pieces_counter = 0
    reverse = False
    for column in range(3):
        for row in range(16):
            if reverse:
                if placement_counter % 4 == 3:
                    array_of_board[column][row] = "X"
                    x_pieces_counter += 1
                if placement_counter % 4 == 1:
                    array_of_board[column - column - column - 1][row] = "O"
                    o_pieces_counter += 1
            else:
                if placement_counter % 4 == 1:
                    array_of_board[column][row] = "X"
                    x_pieces_counter += 1
                if placement_counter % 4 == 3:
                    array_of_board[column - column - column - 1][row] = "O"
                    o_pieces_counter += 1

            placement_counter += 1
        if reverse:
            reverse = False
        else:
            reverse = True
    return x_pieces_counter, o_pieces_counter


def print_board():
    x_pieces_counter = 0
    o_pieces_counter = 0
    for column in array_of_board:
        index_of_column = array_of_board.index(column)
        counter_of_row = 0
        for row in column:
            if row == "X":
                if X_queens[index_of_column][counter_of_row] == 1:
                    print(Fore.MAGENTA + row + Fore.RESET, end=" ")
                    x_pieces_counter += 1
                else:
                    print(Fore.RED + row + Fore.RESET, end=" ")
                    x_pieces_counter += 1
            elif row == "O":
                if O_queens[index_of_column][counter_of_row] == 1:
                    print(Fore.BLUE + row + Fore.RESET, end=" ")
                    o_pieces_counter += 1
                else:
                    print(Fore.GREEN + row + Fore.RESET, end=" ")
                    o_pieces_counter += 1
            else:
                print(row, end=" ")
            counter_of_row += 1
        print("\n", end="")
    print(end="\n")


def print_helping_board():
    copy_of_array_of_board = array_of_board.copy()
    counter = 1
    x_pieces_counter = 0
    o_pieces_counter = 0
    for column in copy_of_array_of_board:
        for row in column:
            if row == "X":
                array_of_X_pieces.append(counter)
                counter += 1
                x_pieces_counter += 1
            elif row == "O":
                array_of_O_pieces.append(counter)
                counter += 1
                o_pieces_counter += 1
            elif row == " ":
                counter += 1
    print(Fore.WHITE, end="")

    for column in array_of_board_helping:
        for row in column:
            index_of_column = array_of_board_helping.index(column)
            index_of_row = column.index(row)
            if row in array_of_X_pieces:
                corrections_and_detections.print_helping_nums(index_of_column, index_of_row, row, "X")
            elif row in array_of_O_pieces:
                corrections_and_detections.print_helping_nums(index_of_column, index_of_row, row, "O")
            else:
                if not row == "|" and row < 10:
                    print(Fore.WHITE + f" {row}" + Fore.WHITE, end=" ")
                else:
                    print(Fore.WHITE + f"{row}" + Fore.WHITE, end=" ")
        print("\n", end="")
    print(Fore.RESET, end="")
    print(end="\n")

    return x_pieces_counter, o_pieces_counter


# Rozdeleni metody move_piece
def piece_interactions(self, name, texts):
    is_choosing = True
    while is_choosing:
        moving_piece = corrections_and_detections.input_correction(texts["select"])
        column_index_of_moving_piece = 0
        row_index_of_moving_piece = 0
        queen_playing = False
        queen_is_capturing = False
        for index, value in enumerate(array_of_board_helping):
            if moving_piece in array_of_board_helping[index]:
                column_index_of_moving_piece = index
                tempo_index = array_of_board_helping[index]
                row_index_of_moving_piece = tempo_index.index(moving_piece)
        if self:
            indicator_of_moving_element = "X"
            enemy_piece = "O"
            column_possible_move = 1
        else:
            indicator_of_moving_element = "O"
            enemy_piece = "X"
            column_possible_move = -1

        if ((array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] == "X" and self)
                or (array_of_board[column_index_of_moving_piece][row_index_of_moving_piece] == "O" and not self)):
            possible_capture_moves = []
            column_of_captured_piece = 0
            row_of_captured_piece = 0
            coo_of_potential_capture_able_pieces = {}
            dict_of_capture_nums = {}
            if (X_queens[column_index_of_moving_piece][row_index_of_moving_piece] == 1 or
                    O_queens[column_index_of_moving_piece][row_index_of_moving_piece] == 1):
                possible_moves = queen.Queen(column_index_of_moving_piece, row_index_of_moving_piece, texts).queen_movement()
                queen_playing = True
                return_array = queen.Queen(column_index_of_moving_piece, row_index_of_moving_piece, texts).queen_capture(
                    enemy_piece)
                if type(return_array[0]) == list:
                    for item in return_array[0]:
                        possible_capture_moves.append(item)
                else:
                    possible_capture_moves = return_array[0]
                column_of_captured_piece = return_array[1]
                row_of_captured_piece = return_array[2]
                dict_of_capture_nums = return_array[4]
                coo_of_potential_capture_able_pieces = return_array[5]
                if dict_of_capture_nums:
                    queen_is_capturing = True

            else:
                return_array = corrections_and_detections.available_moves_normal(
                    column_index_of_moving_piece, row_index_of_moving_piece,
                    column_possible_move, enemy_piece
                )
                if len(return_array) > 2:
                    possible_moves = return_array[0]
                    possible_capture_moves = return_array[1]
                    column_of_captured_piece = return_array[2]
                    row_of_captured_piece = return_array[3]
                    coo_of_potential_capture_able_pieces = return_array[5]
                    dict_of_capture_nums = return_array[6]
                else:
                    possible_moves = return_array[0]
                    possible_capture_moves = return_array[1]

            if possible_moves and possible_capture_moves:
                for num in possible_capture_moves:
                    if num in possible_moves:
                        possible_moves.remove(num)
            if not possible_moves and not possible_capture_moves:
                print(texts["cant_be_moved"].format(moving_piece=moving_piece))
            else:
                if possible_moves:
                    print(texts["possible_moves"].format(moving_piece=moving_piece, possible_moves=' '.join(map(str, possible_moves))))
                if possible_capture_moves:
                    for key, value in dict_of_capture_nums.items():
                        if queen_is_capturing:
                            print(texts["can_capture"].format(key=key, value=value))
                        else:
                            print(texts["can_capture"].format(key=key, value=' '.join(map(str, value))))
                is_choosing_move = True
                while is_choosing_move:
                    is_capturing = False
                    final_move = corrections_and_detections.input_correction(texts["move"])
                    if final_move in possible_moves:
                        final_array_of_moves = possible_moves
                    else:
                        final_array_of_moves = possible_capture_moves
                        is_capturing = True

                    for num in final_array_of_moves:
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
                                        elif indicator_of_moving_element == "O":
                                            if queen_playing:
                                                O_queens[column_index_of_moving_piece][row_index_of_moving_piece] = "|"
                                                O_queens[final_column][final_row] = 1
                                            array_of_board[final_column][final_row] = "O"
                                        if is_capturing:
                                            if coo_of_potential_capture_able_pieces:
                                                for key, value in coo_of_potential_capture_able_pieces.items():
                                                    if key == final_move:
                                                        column_of_captured_piece = value[0]
                                                        row_of_captured_piece = value[1]
                                            array_of_board[column_of_captured_piece][row_of_captured_piece] = " "
                                        array_of_O_pieces.clear()
                                        array_of_X_pieces.clear()
                                        queen.Queen(final_column, final_row, texts).has_queen(self, name)
                                        is_choosing_move = False
                                        print(f"X: {X_queens}")
                                        print(f"O: {O_queens}")
                                        is_choosing = False
