from colorama import Fore
from values import *


class Queen:
    def __init__(self, index_of_column, index_of_row):
        self.index_of_column = index_of_column
        self.index_of_row = index_of_row

    def has_queen(self, player, name):
        if player and self.index_of_column == 7:
            print(f"Player {name} obtained queen.")
            print(f"Colum: {self.index_of_column}, Row: {self.index_of_row}")

            X_queens[self.index_of_column][self.index_of_row] = True

        elif not player and self.index_of_column == 0:
            print(f"Player {name} obtained queen.")
            print(f"Colum: {self.index_of_column}, Row: {self.index_of_row}")

            O_queens[self.index_of_column][self.index_of_row] = 1

    def queen_movement(self):
        final_result = []
        column_increase = 1

        #Zlepseni kodu
        for num in range(4):
            row_increase = 1
            if 0 <= num <= 1:
                column_increase = 1
            elif 2 <= num <= 3:
                column_increase = -1
            if num % 2 == 0:
                row_increase = 2
            elif num % 2 == 1:
                row_increase = -2

            while True:
                if not -15 <= self.index_of_row + row_increase <= 15 or not 0 <= self.index_of_column + column_increase <= 7:
                    break
                try:
                    if array_of_board[self.index_of_column + column_increase][self.index_of_row + row_increase] == " ":
                        final_result.append(array_of_board_helping[self.index_of_column + column_increase][
                                                self.index_of_row + row_increase])
                except IndexError:
                    break
                if row_increase > 0:
                    row_increase += 2
                else:
                    row_increase -= 2

                if column_increase > 0:
                    column_increase += 1
                elif column_increase < 0:
                    column_increase -= 1

        return final_result


def print_pieces(index_of_column, index_of_row, row, indicator):
    if (X_queens[index_of_column][index_of_row] == 1 or
            O_queens[index_of_column][index_of_row] == 1):
        #Zbavit se duplicity
        if indicator == "X":
            if row < 10:
                print(Fore.MAGENTA + f" {row}" + Fore.WHITE, end=" ")
            else:
                print(Fore.MAGENTA + f"{row}" + Fore.WHITE, end=" ")
        elif indicator == "O":
            if row < 10:
                print(Fore.BLUE + f" {row}" + Fore.WHITE, end=" ")
            else:
                print(Fore.BLUE + f"{row}" + Fore.WHITE, end=" ")

    else:
        if indicator == "X":
            if row < 10:
                print(Fore.RED + f" {row}" + Fore.WHITE, end=" ")
            else:
                print(Fore.RED + f"{row}" + Fore.WHITE, end=" ")
        elif indicator == "O":
            if row < 10:
                print(Fore.GREEN + f" {row}" + Fore.WHITE, end=" ")
            else:
                print(Fore.GREEN + f"{row}" + Fore.WHITE, end=" ")
