import random

import datetime
import board
import corrections_and_detections
from languages import language
from informations import measuring
from arrays import X_queens, O_queens

first_player_total_pieces = 12
second_player_total_pieces = 12


def choose_language():
    while True:
        select_language = input(
            "Choose between czech [cs] or english [en] / "
            "Vyber si mezi češtinou [cs] nebo angličtinou [en]: "
        )
        if select_language == "cs":
            return language("cs")
        elif select_language == "en":
            return language("en")
        else:
            print("Incorrect choice / Neplatná volba")


def gameplay_method(first_player_name, second_player_name, first_play, texts):
    if first_play == 1:
        starting_player = first_player_name
        next_player = second_player_name
        starting_players_piece = "(X)"
        next_players_piece = "(O)"
        playing_variable = False
    else:
        starting_player = second_player_name
        next_player = first_player_name
        starting_players_piece = "(O)"
        next_players_piece = "(X)"
        playing_variable = True

    print(texts["begins"].format(starting_player=starting_player))
    print(end="\n")
    is_finished = False
    while True:
        for num in range(2):
            if num == 0:
                playing_player = starting_player
                playing_player_pieces = starting_players_piece
            else:
                playing_player = next_player
                playing_player_pieces = next_players_piece

            playing_variable = corrections_and_detections.playing_variable_check(playing_variable)

            print("------------------------------------------")
            print(texts["Playing"].format(playing_player=playing_player, playing_player_pieces=playing_player_pieces))
            print(end="\n")
            board.print_board()
            board.print_helping_board()
            board.piece_interactions(playing_variable, playing_player, texts)

            all_pieces = corrections_and_detections.players_pieces_check()
            first_player_total_pieces = all_pieces[0]
            second_player_total_pieces = all_pieces[1]

            if first_player_total_pieces == 0 or second_player_total_pieces == 0:
                if first_player_total_pieces == 0:
                    print(texts["Second_won"].format(second_player_name=second_player_name))
                    winner = second_player_name
                    
                else:
                    print(texts["First_won"].format(first_player_name=first_player_name))
                    winner = first_player_name
                is_finished = True
                break

        if is_finished:
            return winner


def game(texts):
    is_playing = True
    board.create_helping_board()
    
    first_player_name = str(input(texts["First_player_name"])).strip()
    second_player_name = str(input(texts["Second_player_name"])).strip()
    score = {first_player_name: 0, second_player_name: 0}
    while is_playing:
        board.create_board()
        board.create_figures()

        who_begins_num = random.randint(1, 2)
        start_time = datetime.datetime.now()
        print(texts["First_player_piece"].format(first_player_name=first_player_name))
        print(texts["Second_player_piece"].format(second_player_name=second_player_name))

        if who_begins_num == 1:
            winner = gameplay_method(first_player_name, second_player_name, who_begins_num, texts)

        elif who_begins_num == 2:
            winner = gameplay_method(first_player_name, second_player_name, who_begins_num, texts)

        print(end="\n")
        measuring(winner, start_time)
        score[winner] += 1
        print(texts["final_score"].format(first_player_name=first_player_name, second_player_name=second_player_name, first_player_score=score[first_player_name], second_player_score=score[second_player_name]))
        print(texts["again"])
    
        while True:
            play_again = input(texts["answer"].format(yes=texts["yes"], no=texts["no"]))
            print()

            if play_again == texts["no"]:
                is_playing = False
                print(texts["End"])
                break
            elif play_again == texts["yes"]:
                corrections_and_detections.queen_array_clean(X_queens)
                corrections_and_detections.queen_array_clean(O_queens)
                break
            else:
                print(texts["Incorrect"])


if __name__ == '__main__':
    game(choose_language())
