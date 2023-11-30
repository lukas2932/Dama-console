def has_queen(self, column, name):
    if self and column == 7:
        print(f"Player {name} obtained queen.")
    elif not self and column == 0:
        print(f"Player {name} obtained queen.")
