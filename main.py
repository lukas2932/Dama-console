import board
import random
import methods
from board import *
from values import first_player_total_pieces, second_player_total_pieces


def gameplay_method(first_player_name, second_player_name, first_play):
    if first_play == 1:
        starting_player = first_player_name
        next_player = second_player_name
        starting_players_piece = "(X)"
        next_players_piece = "(O)"
    else:
        starting_player = second_player_name
        next_player = first_player_name
        starting_players_piece = "(O)"
        next_players_piece = "(X)"

    print(f"Player {starting_player} begins as first.")
    print(end="\n")

    playing_variable = True
    gameplay = True
    while gameplay:
        if first_player_total_pieces == 0 or second_player_total_pieces == 0:
            gameplay = False

        playing_variable = methods.playing_variable_check(playing_variable)

        print("------------------------------------------")
        print(f"{starting_player}{starting_players_piece} is playing.")
        print(end="\n")
        board.print_board()
        board.print_helping_board()
        move_piece(playing_variable, second_player_name)

        playing_variable = methods.playing_variable_check(playing_variable)

        print("------------------------------------------")
        print(f"{next_player}{next_players_piece} is playing.")
        print(end="\n")
        board.print_board()
        board.print_helping_board()
        move_piece(playing_variable, first_player_name)


def game():
    is_playing = True
    board.create_helping_board()

    while is_playing:
        board.create_board()
        board.create_figures()

        first_player_name = str(input("First player name: ")).strip()
        second_player_name = str(input("Second player name: ")).strip()

        who_begins_num = random.randint(1, 2)
        print(end="\n")

        print(f"{first_player_name}'s pieces are X.")
        print(f"{second_player_name}'s pieces are O.")

        if who_begins_num == 1:
            gameplay_method(first_player_name, second_player_name, who_begins_num)

        elif who_begins_num == 2:
            gameplay_method(first_player_name, second_player_name, who_begins_num)

        print(end="\n")
        print("Do you want to play again?")
        play_again = input("Answer(yes / no): ")

        if play_again == "no":
            print("End")
            is_playing = False


if __name__ == '__main__':
    game()
