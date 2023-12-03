import board
import random
from board import *
from values import first_player_total_pieces, second_player_total_pieces
from languages import language

def choose_language():
    while True:
        select_language = input("Choose between czech [cs] or english [en] | Vyber si mezi češtinou [cs] nebo angličtinou [en]: ")
        if select_language == "cs":
            return language("cs") 
        elif select_language == "en":
            return language("en")
        else:
            print("Neplatná volba")

def game(texts):
    is_playing = True
    board.create_helping_board()
    #Zlepseni kodu, rozdeleni metody
    while is_playing:
        board.create_board()
        board.create_figures()

        first_player_name = str(input(texts["First_player"])).strip()
        second_player_name = str(input(texts["Second player name: "])).strip()

        who_begins_num = random.randint(1, 2)
        print(end = "\n")

        if who_begins_num == 1:
            print(texts["first_player_name's pieces are X."].format(first_player_name=first_player_name))
            print(texts["second_player_name's pieces are O."].format(second_player_name=second_player_name))
            print(texts["Player first_player_name begins as first."].format(first_player_name=first_player_name))
            
            print(end = "\n")

            playing_variable = True
            gameplay = True
            while gameplay:
                if first_player_total_pieces == 0 or second_player_total_pieces == 0:
                    gameplay = False
                if playing_variable:
                    print("------------------------------------------")
                    print(texts["first_player_name(X) is playing."].format(first_player_name=first_player_name))
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, second_player_name)
                    playing_variable = False
                else:
                    print("------------------------------------------")
                    print(texts["second_player_name(O) is playing"].format(second_player_name=second_player_name))
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, first_player_name)
                    playing_variable = True

        elif who_begins_num == 2:
            print(texts["first_player_name(X) is playing."].format(first_player_name=first_player_name))
            print(texts["second_player_name(O) is playing"].format(second_player_name=second_player_name))
            print(texts["second_player_name begins"].format(second_player_name=second_player_name))
            print(end = "\n")

            playing_variable = False
            gameplay = True
            while gameplay:
                if first_player_total_pieces == 0 or second_player_total_pieces == 0:
                    gameplay = False

                if playing_variable:
                    print("------------------------------------------")
                    print(texts["first_player_name(X) is now playing."].format(first_player_name=first_player_name))
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, second_player_name)
                    playing_variable = False
                else:
                    print("------------------------------------------")
                    print(texts["second_player_name(O) is now playing."].format(second_player_name=second_player_name))
                    print(end= "\n")
                    board.print_board()
                    board.print_helping_board()
                    move_piece(playing_variable, first_player_name)
                    playing_variable = True

        print(end="\n")
        print(texts["Again"])
        play_again = input("Answer(yes / no): ")


        if play_again == "no":
            print(texts["END"])
            is_playing = False


if __name__ == '__main__':
    game(choose_language())
