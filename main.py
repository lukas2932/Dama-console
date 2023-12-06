import board
import random
from board import *

first_player_total_pieces = 12
second_player_total_pieces = 12


def gameplay_method(first_player_name, second_player_name, first_play):
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

    print(f"Player {starting_player} begins as first.")
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
            print(f"{playing_player}{playing_player_pieces} is playing.")
            print(end="\n")
            board.print_board()
            board.print_helping_board()
            move_piece(playing_variable, enemy_player)

            all_pieces = methods.players_pieces_check()
            first_player_total_pieces = all_pieces[0]
            second_player_total_pieces = all_pieces[1]

            if first_player_total_pieces == 1 or second_player_total_pieces == 1:
                if first_player_total_pieces == 0:
                    print(f"f{first_player_name} won.")
                else:
                    print(f"f{second_player_name} won.")
                is_finished = True
                break

        if is_finished:
            break


def game():
    is_playing = True
    board.create_helping_board()

    while is_playing:
        board.create_board()
        board.create_figures()

        first_player_name = str(input("First player name: ")).strip()
        second_player_name = str(input("Second player name: ")).strip()

        who_begins_num = random.randint(1, 2)
        print(who_begins_num)
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
