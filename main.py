import board
import random
from board import *
from languages import language

first_player_total_pieces = 12
second_player_total_pieces = 12

def choose_language():
    while True:
        select_language = input("Choose between czech [cs] or english [en] / Vyber si mezi češtinou [cs] nebo angličtinou [en]: ")
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
                enemy_player = second_player_name
                playing_player = starting_player
                playing_player_pieces = starting_players_piece
            else:
                enemy_player = first_player_name
                playing_player = next_player
                playing_player_pieces = next_players_piece

            playing_variable = methods.playing_variable_check(playing_variable)

            print("------------------------------------------")
            print(texts["Playing"].format(playing_player=playing_player, playing_player_pieces=playing_player_pieces))
            print(end="\n")
            board.print_board()
            board.print_helping_board()
            move_piece(playing_variable, enemy_player, texts)

            all_pieces = methods.players_pieces_check()
            first_player_total_pieces = all_pieces[0]
            second_player_total_pieces = all_pieces[1]

            if first_player_total_pieces == 1 or second_player_total_pieces == 1:
                if first_player_total_pieces == 0:
                    print(texts["First_won"].format(first_player_name=first_player_name))
                else:
                   print(texts["Second_won"].format(second_player_name=second_player_name))
                is_finished = True
                break

        if is_finished:
            break


def game(texts):
    is_playing = True
    board.create_helping_board()

    while is_playing:
        board.create_board()
        board.create_figures()

        first_player_name = str(input(texts["First_player_name"])).strip()
        second_player_name = str(input(texts["Second_player_name"])).strip()

        who_begins_num = random.randint(1, 2)
        print(who_begins_num)
        print(end="\n")

        print(texts["First_player_piece"].format(first_player_name=first_player_name))
        print(texts["Second_player_piece"].format(second_player_name=second_player_name))

        if who_begins_num == 1:
            gameplay_method(first_player_name, second_player_name, who_begins_num, texts)

        elif who_begins_num == 2:
            gameplay_method(first_player_name, second_player_name, who_begins_num, texts)

        print(end="\n")
        print(texts["again"])

        while True:
            play_again = input(texts["answer"].format(yes=texts["yes"], no=texts["no"]))
            print()

            if play_again == texts["no"]:
                is_playing = False
                print(texts["End"])
                break
            elif play_again == texts["yes"]:
                break
            else:
                print(texts["Incorrect"])

if __name__ == '__main__':
    game(choose_language())
