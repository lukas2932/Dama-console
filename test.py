import pytest

import board
import corrections_and_detections


@pytest.mark.parametrize('playing_variable, expected', [
    (False, True),
    (True, False)
])
def test_playing_variable_check(playing_variable, expected):
    result = corrections_and_detections.playing_variable_check(playing_variable)
    assert result == expected


def test_create_figures():
    board.create_board()
    final_array = board.create_figures()
    result_1 = final_array[0]
    result_2 = final_array[1]

    final_result = result_1 == result_2
    assert final_result


def test_players_pieces_check():
    board.create_board()
    final_figure_array = board.create_figures()
    result_figure_1 = final_figure_array[0]
    result_figure_2 = final_figure_array[1]

    final_pieces_array = corrections_and_detections.players_pieces_check()
    result_pieces_1 = final_pieces_array[0]
    result_pieces_2 = final_pieces_array[1]

    final_result_1 = result_figure_1 == result_pieces_1
    final_result_2 = result_figure_2 == result_pieces_2
    assert final_result_1, final_result_2


@pytest.mark.parametrize('user_input, expected', [
    ("ahoj", False),
    (22, True)
])
def test_input_correction(user_input, expected):
    try:
        input = int(user_input)
        final_result = True
    except:
        final_result = False
        pass

    assert final_result == expected