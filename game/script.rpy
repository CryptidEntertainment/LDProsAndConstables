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
default player_pronoun_cap_subject = "They"
default player_pronoun_cap_object = "Them"
default player_pronoun_cap_possessive = "Their"

default day_index = 0

image mom = "chicken.png"
image shit = "shit.png"
image sir = "sir.png"
image hair = "hair.png"

label start:
    call l_intro
    
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

label l_intro:
    
    $ renpy.pause(3)
    
    show sir at left with vpunch
    
    "HALT!"
    
    
    
    
    
    menu:
        "State your pronouns!"
        
        "They/them":
            $ player_pronoun_subject = "they"
            $ player_pronoun_object = "them"
            $ player_pronoun_possessive = "their"
            $ player_pronoun_verb = "are"
            $ player_pronoun_cap_subject = "They"
            $ player_pronoun_cap_object = "Them"
            $ player_pronoun_cap_possessive = "Their"
        "He/him":
            $ player_pronoun_subject = "he"
            $ player_pronoun_object = "him"
            $ player_pronoun_possessive = "his"
            $ player_pronoun_verb = "is"
            $ player_pronoun_cap_subject = "He"
            $ player_pronoun_cap_object = "Him"
            $ player_pronoun_cap_possessive = "His"
        "She/her":
            $ player_pronoun_subject = "she"
            $ player_pronoun_object = "her"
            $ player_pronoun_possessive = "her"
            $ player_pronoun_verb = "is"
            $ player_pronoun_cap_subject = "She"
            $ player_pronoun_cap_object = "Her"
            $ player_pronoun_cap_possessive = "Her"
    
    "Oh."
    "Effrafax of Wug, is that you?"
    
    menu:
        "It's hard to see in the dark."
        
        "Surely the helmet is not helping, Captain Sir.":
            "What? My helmet is fine! Show some respect!"
        "It sure is, Captain Sir!":
            "Show some respec— oh. Yes. Yes, it is."
    
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