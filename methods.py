from colorama import Fore
from values import X_queens, O_queens, array_of_board, array_of_board_helping


class Queen:
    def __init__(self, index_of_column, index_of_row, texts):
        self.index_of_column = index_of_column
        self.index_of_row = index_of_row
        self.texts = texts

    def has_queen(self, player, name):
        if player and self.index_of_column == 7:
            print(self.texts["obtained_queen"].format(name=name))

            X_queens[self.index_of_column][self.index_of_row] = True

        elif not player and self.index_of_column == 0:
            print(self.texts["obtained_queen"].format(name=name))
            
            O_queens[self.index_of_column][self.index_of_row] = 1

    def queen_movement(self):
        final_result = []
        for num in range(4):
            if 0 <= num <= 1:
                column_increase = 1
            else:
                column_increase = -1
            if num % 2 == 0:
                row_increase = 2
            else:
                row_increase = -2

            while True:
                if not -15 <= self.index_of_row + row_increase <= 15 or not 0 <= self.index_of_column + column_increase <= 7:
                    break
                try:
                    if array_of_board[self.index_of_column + column_increase][self.index_of_row + row_increase] == " ":
                        final_result.append(array_of_board_helping[self.index_of_column + column_increase][
                                                self.index_of_row + row_increase])
                    if not array_of_board[self.index_of_column + column_increase][
                               self.index_of_row + row_increase] == " ":
                        break
                except IndexError:
                    break
                if row_increase > 0:
                    row_increase += 2
                else:
                    row_increase -= 2

                if column_increase > 0:
                    column_increase += 1
                else:
                    column_increase -= 1

        return final_result

    def queen_capture(self, enemy_piece):
        final_result = []
        column_of_captured_piece = 0
        row_of_captured_piece = 0
        captured_num_in_helping_board = 0
        dict_of_capture_nums = {}
        coo_of_potential_capture_able_pieces = {}
        for num in range(4):
            enemy_piece_confirmed = False
            if 0 <= num <= 1:
                column_increase = 1
            else:
                column_increase = -1
            if num % 2 == 0:
                row_increase = 2
            else:
                row_increase = -2
            previous_column_increase = 0
            previous_row_increase = 0
            for second_num in range(2):
                if not -15 <= self.index_of_row + row_increase <= 15 or not 0 <= self.index_of_column + column_increase <= 7:
                    break
                try:
                    if enemy_piece_confirmed:
                        if array_of_board[self.index_of_column + column_increase][
                            self.index_of_row + row_increase] != " ":
                            enemy_piece_confirmed = False
                            continue
                        else:
                            final_result.append(array_of_board_helping[self.index_of_column + column_increase][
                                                    self.index_of_row + row_increase])
                            column_of_captured_piece = self.index_of_column + previous_column_increase
                            row_of_captured_piece = self.index_of_row + previous_row_increase
                            captured_num_in_helping_board = array_of_board_helping[column_of_captured_piece][
                                row_of_captured_piece]
                            dict_of_capture_nums[captured_num_in_helping_board] = \
                                array_of_board_helping[self.index_of_column + column_increase][
                                    self.index_of_row + row_increase]
                            coo_of_potential_capture_able_pieces[
                                array_of_board_helping[self.index_of_column + column_increase][
                                    self.index_of_row + row_increase]] = column_of_captured_piece, row_of_captured_piece
                            break
                    if array_of_board[self.index_of_column + column_increase][
                        self.index_of_row + row_increase] == enemy_piece and not enemy_piece_confirmed:
                        enemy_piece_confirmed = True
                        previous_column_increase = column_increase
                        previous_row_increase = row_increase

                except IndexError:
                    pass
                if enemy_piece_confirmed:
                    if row_increase > 0:
                        row_increase += 2
                    else:
                        row_increase -= 2

                    if column_increase > 0:
                        column_increase += 1
                    else:
                        column_increase -= 1
        return (final_result, column_of_captured_piece, row_of_captured_piece,
                captured_num_in_helping_board, dict_of_capture_nums, coo_of_potential_capture_able_pieces)


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
