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
default day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

image mom = "chicken.png"
image shit = "shit.png"
image sir = "sir.png"
image hair = "hair.png"
image urchin = "derp.png"
image merchant = "hat.png"
image drunkard = "beer.png"

label start:
    call l_intro
    
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
    
    cap_unknown "Alright then, trainee. My name is Captain Louis Sirr, Guard Captain of the City Constables. I'm going to teach you about being a proper Constable."
    
    menu:
        cap "Are you ready, recruit? These next few days are going to be rough if you're unprepared."
        "Yes sir.":
            cap "What did you just say to me?"
            
            menu:
                cap "I don't think I heard you."
                "Sir, yes sir!":
                    cap "Now, that's what I like to hear! First, we'll begin with your equipment..."
                    #!!!!!
                "I, um, think I'm ready, sir?":
                    # Guard Captain Sir puts his head in his hands and sighs.
                    cap "We're going to have to work on that. Alright, let's start with scrubbing the chamber pots..."
                    #!!!!!
            
        "I don't think I'm ready yet.":
            cap "Well then, what are you doing here? This training is for those who want to be a guard! Don't waste my time."
            
            $ renpy.pause(1)
            hide sir with dissolve
            $ renpy.pause(2)
            
            "Well, shit."
            
            $ renpy.pause(1)
            
            return
    
    $ renpy.pause(1)
    hide sir with dissolve
    $ renpy.pause(2)
    
    "A year ago, I had enlisted to join the City Constables. It was the day that I matured into a real adult: my 16th birthday."
    "But I've been stagnating. Doing the same thing every single day, from wake to sleep, day in, day out."
    "Wake up in the barracks."
    "Stand on the street corner in the morning."
    "Make the rounds about the marketplace in the afternoon."
    "Report about the day to the Guard Captain."
    "Prepare for the next day and go to sleep."
    "I need to make a change. It's been on my mind for the last few months now, but I haven't had the time or energy to commit to changing anything."
    "You know what? Screw it. Waiting forever and continuing to suffer sucks."
    "If nothing changes by the end of the week, I'm gonna quit."
    "Maybe I'll become a baker."
    "(...but I don't even know how to bake bread...)"
    "Whatever. I'll burn that bridge when I get to it."
    "This week, I'm going to do something different. Maybe it'll go well, maybe it'll suck."
    "But by the end of this week, either I'm going to be happy about my job, or I'll quit and live my life anew."
    "That... That sounds pretty good."
    "..."
    "(Am I having my midlife crisis?)"
    "(My life expectancy is around 35...)"
    "(Ah, shit.)"
    "..."
    "Well. Today is Monday, and it's the beginning of another work day."
    "I should get ready to work."
    
    jump l_cycle
    
    return

label l_cycle:
    $ day_index_sub = 5 - day_index
    $ day_index_name = day_names[day_index]
    
    "It’s the crack of dawn, and the sun has begun rising."
    "Today is [day_index_name], with [day_index_sub] days until the end of the week."
    "Time to don my chainmail and get ready for work."
    menu:
        "Grab your mace and get out there":
            pass

    call l_morning
    call l_afternoon
    call l_night
    
    $ day_index += 1
    
    if day_index < 5:
        jump l_cycle
    
    return

label l_morning:
    "Morning"
    return

label l_afternoon:
    "Afternoon"
    return

label l_night:
    "Night"
    return