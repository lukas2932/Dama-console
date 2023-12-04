def language(choice):
    texts = {
        "First_player": {"en": "First player name: ", "cs": "Jméno prvního hráče: "},
        "Second player name: ": {"en": "Second player name: ", "cs": "Jméno druhého hráče: "},
        "first_player_name's pieces are X.": {"en": "{first_player_name}'s pieces are X.", "cs": "{first_player_name} figurky jsou X."},
        "second_player_name's pieces are O.": {"en": "{second_player_name}'s pieces are O.", "cs": "{second_player_name} figurky jsou O."},
        "first_player_name(X) is playing.": {"en": "{first_player_name}(X) is playing.", "cs": "{first_player_name}(X) hraje."},
        "second_player_name(O) is playing": {"en": "{second_player_name}(O) is playing", "cs": "{second_player_name}(O) hraje."},
        "first_player_name(X) is playing.": {"en": "{first_player_name}(X) is playing", "cs": "{first_player_name}(X) hraje."},
        "second_player_name(O) is playing": {"en": "{second_player_name}(O) is playing", "cs": "{second_player_name}(O) hraje."},
        "second_player_name begins": {"en": "{second_player_name} begins as first", "cs": "{second_player_name} hraje první"},
        "first_player_name(X) is now playing.": {"en": "{first_player_name}(X) is playing", "cs": "{first_player_name}(X) hraje."},
        "second_player_name(O) is now playing.": {"en": "{second_player_name}(O) is playing", "cs": "{second_player_name}(O) hraje."},
        "Player first_player_name begins as first." : {"en": "{first_player_name} begins as first", "cs": "{first_player_name} hraje první"},
        "Again": {"en": "Do you want to play again?", "cs": "Chceš hrát znovu?"},
        "END": {"en": "You have finished the game", "cs": "Ukončil jsi hru"}
    }

    return {text: texts[text][choice] for text in texts}
    