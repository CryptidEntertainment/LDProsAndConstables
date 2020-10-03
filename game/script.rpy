# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default status_urchin = 0
default status_thief = 0
default status_mom = 0
default status_guards = 0
default status_guard_captain = 0
default status_merchant = 0

default player_pronoun_subject = "they"
default player_pronoun_object = "them"
default player_pronoun_possessive = "their"
default player_pronoun_verb = "are"

default day_index = 0

label start:
    call l_set_pronouns
    
    #jump l_loop
    
    return

label l_loop:
    call l_loop_morning
    call l_loop_afternoon
    call l_loop_checkin
    call l_loop_evening
    
    $ day_index += 1
    
    if day_index > 3:
        return
    
    jump l_loop

label l_loop_morning:
    "It is morning"
    return

label l_loop_afternoon:
    "It is afternoon"
    return

label l_loop_checkin:
    "It is checkin time"
    return

label l_loop_evening:
    "It is evening"
    return

label l_set_pronouns:
    menu:
        "Your preferred pronouns?"
        
        "They/them":
            $ player_pronoun_subject = "they"
            $ player_pronoun_object = "them"
            $ player_pronoun_possessive = "their"
            $ player_pronoun_verb = "are"
        "He/him":
            $ player_pronoun_subject = "he"
            $ player_pronoun_object = "him"
            $ player_pronoun_possessive = "his"
            $ player_pronoun_verb = "is"
        "She/her":
            $ player_pronoun_subject = "she"
            $ player_pronoun_object = "her"
            $ player_pronoun_possessive = "her"
            $ player_pronoun_verb = "is"
    
    "[player_pronoun_subject] went to the supermarket."
    "That was not very nice of [player_pronoun_object]."
    "This is [player_pronoun_possessive] pineapple."
    "[player_pronoun_subject] [player_pronoun_verb] in quarantine until Christmas."
    
    return

label l_urchin:
    e "You have visited the urchin!"
    $ status_urchin += 1
    jump l_menu_post

label l_thief:
    e "You have visited the thief!"
    $ status_thief += 1
    jump l_menu_post

label l_merchant:
    e "You have visited the merchant!"
    $ status_merchant += 1
    jump l_menu_post