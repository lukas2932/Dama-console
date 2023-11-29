import board
import random
from board import *

def game():
    is_playing = True
    board.create_helping_board()

    while is_playing:
        board.create_board()
        board.create_figures()

        first_player_name = str(input("First player name: "))
        second_player_name = str(input("Second player name: "))

        who_begins_num = random.randint(1, 2)
        print(end = "\n")

        if who_begins_num == 1:
            print(f"{first_player_name}'s pieces are X.")
            print(f"{second_player_name}'s pieces are O.")
            print(f"Player {first_player_name} begins as first.")
            print(end = "\n")

            playing_variable = True
            gameplay = True
            while gameplay:
                if first_player_total_pieces == 0 or second_player_total_pieces == 0:
                    gameplay = False
                if playing_variable:
                    print("------------------------------------------")
                    print(f"{first_player_name}(X) is playing.")
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, second_player_name)
                    playing_variable = False
                else:
                    print("------------------------------------------")
                    print(f"{second_player_name}(O) is playing.")
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, first_player_name)
                    playing_variable = True

        elif who_begins_num == 2:
            print(f"{first_player_name}'s pieces are X.")
            print(f"{second_player_name}'s pieces are O.")
            print(f"Player {second_player_name} begins as first.")
            print(end = "\n")

            playing_variable = False
            gameplay = True
            while gameplay:
                if first_player_total_pieces == 0 or second_player_total_pieces == 0:
                    gameplay = False

                if playing_variable:
                    print("------------------------------------------")
                    print(f"{first_player_name}(X) is playing.")
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, second_player_name)
                    playing_variable = False
                else:
                    print("------------------------------------------")
                    print(f"{second_player_name}(O) is playing.")
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, first_player_name)
                    playing_variable = True

        print(end="\n")
        print("Do you want to play again?")
        play_again = input("Answer(yes / no): ")


        if play_again == "no":
            print("End")
            is_playing = False


if __name__ == '__main__':
    game()
