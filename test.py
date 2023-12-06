import pytest

import board
import methods


@pytest.mark.parametrize('playing_variable, expected', [
    (False, True),
    (True, False)
])
def test_playing_variable_check(playing_variable, expected):
    result = methods.playing_variable_check(True)
    assert not result


def test_create_figures():
    board.create_board()
    final_array = board.create_figures()
    result_1 = final_array[0]
    result_2 = final_array[1]

    final_result = result_1 == result_2
    assert final_result


def test_players_pieces_check():
    board.create_board()
    final_array = methods.players_pieces_check()
    result_1 = final_array[0]
    result_2 = final_array[1]

    final_result = result_1 == result_2
    assert final_result


def test_create_figures_and_players_pieces_check():
    board.create_board()
    final_figure_array = board.create_figures()
    result_figure_1 = final_figure_array[0]
    result_figure_2 = final_figure_array[1]

    final_pieces_array = methods.players_pieces_check()
    result_pieces_1 = final_pieces_array[0]
    result_pieces_2 = final_pieces_array[1]

    final_result_1 = result_figure_1 == result_pieces_1
    final_result_2 = result_figure_2 == result_pieces_2
    assert final_result_1, final_result_2


def test_print_helping_board_and_print_board():
    board.create_board()
    board.create_figures()

    final_board_array = board.print_board()
    result_board_1 = final_board_array[0]
    result_board_2 = final_board_array[1]

    final_helping_array = board.print_helping_board()
    result_helping_1 = final_helping_array[0]
    result_helping_2 = final_helping_array[1]

    final_result_1 = result_board_1 == result_helping_1
    final_result_2 = result_board_2 == result_helping_2
    assert final_result_1, final_result_2


