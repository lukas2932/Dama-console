def language(choice):
    texts = {
        "begins": {"en": "Player {starting_player} begins as first.", "cs": "Hráč {starting_player} začíná jako první."},
        "obtained_queen": {"en": "Player {name} obtained queen.", "cs": "Hráč {name} získal Dámu."},
        "select": {"en": "Select a piece you want to move: ", "cs": "Vyber figurku, s kterou chceš pohnout: "},
        "cant_be_moved": {"en": "There can not be done any moves to {moving_piece}", "cs": "S touho figurkou nelze pohnout {moving_piece}"},
        "possible_moves": {"en": "Possible moves in {moving_piece} are: {possible_moves}", "cs": "Možné poyhyby pro {moving_piece} jsou: {possible_moves}"},
        "can_capture": {"en": "You can capture {key} by: {value}", "cs": "Můžeš přeskočit {key} s: {value}"},
        "move": {"en": "Move to: ", "cs": "Pohnout na: "},
        "no": {"en": "no", "cs": "ne"},
        "yes": {"en": "yes", "cs": "ano"},
        "answer": {"en": "Answer[{yes} / {no}]: ", "cs": "Odpoveď[{yes} / {no}]: "},
        "End": {"en": "You ended game.", "cs": "Ukončil jsi hru."},
        "Incorrect": {"en": "Incorrect choice", "cs": "Neplatná volba"},
        "again": {"en": "Do you want to play again? ", "cs": "Chceš hrát znovu? "},
        "First_player_piece": {"en": "{first_player_name}'s pieces are X.", "cs": "{first_player_name} má figurky X."},
        "Second_player_piece": {"en": "{second_player_name}'s pieces are O.", "cs": "{second_player_name} má figurky O."},
        "First_player_name": {"en": "First player name: ", "cs": "Jméno prvního hráče: "},
        "Second_player_name": {"en": "Second player name: ", "cs": "Jméno druhého hráče: "},
        "First_won": {"en": "{first_player_name} won.", "cs": "{first_player_name} vyhrál."},
        "Second_won": {"en": "{second_player_name} won.", "cs": "{second_player_name} vyhrál."},
        "Playing": {"en": "{playing_player}{playing_player_pieces} is playing.", "cs": "{playing_player}{playing_player_pieces} právě hraje."}
    }

    return {text: texts[text][choice] for text in texts}
    