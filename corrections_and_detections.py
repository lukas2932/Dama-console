from colorama import Fore
from constants import X_queens, O_queens, array_of_board, array_of_board_helping


def print_helping_nums(index_of_column, index_of_row, row, indicator):
    if indicator == "X":
        queen_color = Fore.MAGENTA
        normal_color = Fore.RED
    else:
        queen_color = Fore.BLUE
        normal_color = Fore.GREEN

    if (X_queens[index_of_column][index_of_row] == 1 or
            O_queens[index_of_column][index_of_row] == 1):
        if row < 10:
            print(queen_color + f" {row}" + Fore.WHITE, end=" ")
        else:
            print(queen_color + f"{row}" + Fore.WHITE, end=" ")

    else:
        if row < 10:
            print(normal_color + f" {row}" + Fore.WHITE, end=" ")
        else:
            print(normal_color + f"{row}" + Fore.WHITE, end=" ")


def playing_variable_check(playing_variable):
    if playing_variable:
        playing_variable = False
    else:
        playing_variable = True

    return playing_variable


def players_pieces_check():
    x_counter = 0
    o_counter = 0
    for column in array_of_board:
        for row in column:
            if row == "X":
                x_counter += 1
            if row == "O":
                o_counter += 1

    return x_counter, o_counter


def available_moves_normal(column_index_of_moving_piece, row_index_of_moving_piece, column_possible_move, enemy_piece):
    result_possible_moves = []
    result_possible_capture_moves = []
    column_of_captured_piece = 0
    row_of_captured_piece = 0
    captured_num_in_helping_board = 0
    coo_of_potential_capture_able_pieces = {}
    dict_of_capture_nums = {}
    is_capturing = False
    for num in range(4):
        if num % 2 == 0:
            moving_row_indicator = 2
            moving_capture_row_indicator = 4
        else:
            moving_row_indicator = -2
            moving_capture_row_indicator = -4
        try:
            if (array_of_board[column_index_of_moving_piece + column_possible_move][
                row_index_of_moving_piece + moving_row_indicator] == " " and
                    array_of_board_helping[column_index_of_moving_piece + column_possible_move][
                        row_index_of_moving_piece + moving_row_indicator] not in result_possible_moves):
                result_possible_moves.append(
                    array_of_board_helping[column_index_of_moving_piece + column_possible_move][
                        row_index_of_moving_piece + moving_row_indicator])

            if (array_of_board[column_index_of_moving_piece + column_possible_move * 2][
                row_index_of_moving_piece + moving_capture_row_indicator] == " " and
                    array_of_board[column_index_of_moving_piece + column_possible_move][
                        row_index_of_moving_piece + moving_row_indicator] == enemy_piece and
                    array_of_board_helping[column_index_of_moving_piece + column_possible_move * 2][
                        row_index_of_moving_piece + moving_capture_row_indicator] not in result_possible_capture_moves):
                result_possible_capture_moves.append(
                    array_of_board_helping[column_index_of_moving_piece + column_possible_move * 2][
                        row_index_of_moving_piece + moving_capture_row_indicator])
                column_of_captured_piece = column_index_of_moving_piece + column_possible_move
                row_of_captured_piece = row_index_of_moving_piece + moving_row_indicator
                captured_num_in_helping_board = array_of_board_helping[column_of_captured_piece][
                    row_of_captured_piece]
                coo_of_potential_capture_able_pieces[
                    array_of_board_helping[column_index_of_moving_piece + column_possible_move * 2][
                        row_index_of_moving_piece + moving_capture_row_indicator]] = (
                    column_of_captured_piece, row_of_captured_piece)
                dict_of_capture_nums[array_of_board_helping[column_of_captured_piece][row_of_captured_piece]] = [
                    array_of_board_helping[column_index_of_moving_piece + column_possible_move * 2][
                        row_index_of_moving_piece + moving_capture_row_indicator]]
                is_capturing = True
        except IndexError:
            pass

    if is_capturing:
        return (result_possible_moves, result_possible_capture_moves,
                column_of_captured_piece, row_of_captured_piece, captured_num_in_helping_board,
                coo_of_potential_capture_able_pieces, dict_of_capture_nums)
    else:
        return result_possible_moves, result_possible_capture_moves


def input_correction(message):
    while True:
        try:
            result = int(input(message))
            return result
        except:
            pass