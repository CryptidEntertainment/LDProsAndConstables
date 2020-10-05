define cap = Character("Captain Louis Sir")
# just in case
define cap_unknown = Character("Captain Louis Sir")

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
image urchin = "derp.png"
image merchant = "hat.png"
image drunkard = "beer.png"

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
    
    cap_unknown "Halt!"
    
    menu:
        cap_unknown "Declare your pronouns!"
        
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
    
    cap "Hmm... is that so."
    
    menu:
        cap "State your business!"
        
        "I just signed up for the City Constables. Do you know where the captain can be found?":
            cap_unknown "Where the captain can be found? I AM the captain!"
        
        "Just looking around.":
            cap_unknown "In a place like this? Bah, you must be one of those idiot new recruits."
        
        "I'm looking for the toilet.":
            cap_unknown "In a place like this?"
            cap_unknown "Down the stairs and on the right."
            cap_unknown "And don't just wander into the barracks next time you need a toilet, citizen! That's a security risk!"
            
            $ renpy.pause(1)
            hide sir with dissolve
            $ renpy.pause(2)
            
            "Down the stairs and on the right is the front door."
            "He seems to be trying to get rid of me."
            
            $ renpy.pause(1)
            
            return
    
    cap_unknown "Alright then, trainee. My name is Captain Louis Sirr, Guard Captain of the City Constables. I’m going to teach you about being a proper Constable."
    
    menu:
        cap "Are you ready, recruit? These next few days are going to be rough if you’re unprepared."
        "Yes sir.":
            cap "What did you just say to me?"
            
            menu:
                cap "I don't think I heard you."
                "Sir, yes sir!":
                    cap "Now, that’s what I like to hear! First, we’ll begin with your equipment..."
                    #!!!!!
                "I, um, think I’m ready, sir?":
                    # Guard Captain Sir puts his head in his hands and sighs.
                    cap "We're going to have to work on that. Alright, let’s start with scrubbing the chamber pots..."
                    #!!!!!
            
        "I don’t think I’m ready yet.":
            cap "Well then, what are you doing here? This training is for those who want to be a guard! Don’t waste my time."
            
            $ renpy.pause(1)
            hide sir with dissolve
            $ renpy.pause(2)
            
            "Well, shit."
            
            $ renpy.pause(1)
            
            return
    
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