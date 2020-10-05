define cap = Character("Captain Louis Sirr")
# just in case
define cap_unknown = Character("Captain Louis Sirr")
define merchant = Character("Merchant")
define thief = Character("Thief")
define unknown = Character("???")
define woman = Character("Woman")
define woman2 = Character("Woman")
define you = Character("You")

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
    
    "It's the crack of dawn, and the sun has begun rising."
    "Today is [day_index_name], with [day_index_sub] days until the end of the week."
    "Time to don my chainmail and get ready for work."
    menu:
        "Grab your mace and get out there":
            pass

    call l_morning
    
    "A couple hours pass, and the sun is a little bit past overhead now. It beats warmly down on my tabard."
    "I can hear the sound of chainmail approaching me. The next Constable should be coming for the afternoon shift."
    "He give me a quick nod as he reaches me, and I take off to go to my afternoon assignment."
    "The sounds of profit - that is, shouting and announcements and haggling - get louder as I approach the marketplace."
    "I hope to myself that nothing terrible happens today."
    "Something always happens, but I just hope it isn't too bad."
    
    call l_afternoon
    
    "The air begins to cool again as the sky darkens. My shift should be over about now."
    "Time to report to Captain Sirr about the day."
    "I walk back into the barracks, and find the Captain in his quarters."
    "Captain Sirr: You're back safe and sound. What happened today?"
    
    call l_night
    
    "The air begins to cool again as the sky darkens. My shift should be over about now."
    "I sigh, and head back to the barracks."
    "And I do the same thing as I do, every night - take off my armor, hang up my tabard, and take out the oil and rag to clean them."
    "My equipment is dusty. Walking the dirt roads all day will do that to them."
    "After a while of polishing and cleaning, it's time to sleep. I lie down on my cot, and pull the woolen blanket over me."
    "Eventually, my eyes turn heavy and the room goes dark."
    
    $ day_index += 1
    
    if day_index < 5:
        jump l_cycle
    
    return

label l_morning:
    "The morning air is still cold when I leave the barracks. The morning dew wets my boots."
    "I walk through the dirt roads until I get to my assigned post."
    "The sun is just over the horizon, now, and my shift begins."
    "Let's see what happens today..."
    
    "PICKPOCKET"
    
    call l_pickpocket
    
    "SWINDLE"
    
    call l_swindle
    
    return

label l_afternoon:
    "Afternoon"
    return

label l_night:
    "Night"
    return

label l_pickpocket:
    "I'm crossing a street when a certain person moving in the crowd catches my eye with the way they're moving."
    "I watch close. He moves up behind a woman, then rushes forward, jostling past her and using the distraction to cut away her coin purse."
    
    menu:
        "What should I do?"
        
        "Ignore it":
            "Damn it, I really don't feel like dealing with thieves right now."
            "Turning my back on the scene, I let it pass and continue my patrol."
            
            # Ignore it (Allied w/ Thieves)
            
            "Must be one of (thief organization player allied with?). Just let him pass..."
            "Pretending not to notice, I continue my patrol."
        
        "Approach the man":
            #(thief: oh, you're making a mistake)
            "I give it some time, keeping my distance as I follow the thief. He's on guard for a minute before he calms down, and I'm able to get closer without him noticing."
            "Moving in behind him, I keep quiet until I'm right on him, and grab his arm hard."
            thief "What?!"
            "He spins back. When he sees me, he struggles, but my grip is solid, he isn't getting away from me that easily."
            "I saw you rob that woman."
            "A grin breaks over his face, both mocking and worried at once."
            thief "Yeah? And what're you gonna do about it?"
            
            menu:
                "Good question."
                
                "Make him give the money back":
                    "You're giving that money back, and then you're going to jail."
                    "His grin widens."
                    thief "How about option three?"
                    "With his free hand, he tosses the coin purse up into the air."
                    "Shit!"
                    "I stagger backward, diving and falling flat on my back as I barely catch the bag to keep it from spilling its contents all over the ground."
                    "Ugh. He got away."
                    "By the time I've recovered and made it back to my feet, the thief is long gone."
                    "At least I got the money back."
                    "After backtracking to where the woman was pickpocketed, I have to search the nearby areas before I find her."
                    "Excuse me, Miss."
                    woman "Yes, constable?"
                    "You were pickpocketed earlier. I recovered your coin purse for you."
                    "As soon as I show her the bag, her hand goes to her waist, searching for the missing purse."
                    woman "Oh, oh my! I didn't even..."
                    woman "Thank you so much!"
                    "Just doing my job."
                    "I hand back her coin purse, and she quickly fastens it back in place, before seeing me off."
                    "As I'm walking away, a random thought comes back to mind."
                    "Did he say \"option three?\" I never gave him an option two..."
                    "Shake my head, laughing a little to myself as I return to my patrol."
                
                "Don't bother":
                    "Nothing."
                    thief "Huh?"
                    "I'm not going to do anything about it."
                    "I crack a grin."
                    "I'm going to let you go, and you’re going to remember it."
                    "You're going to owe me one. Remember that."
                    "The man’s expression turns sour."
                    thief "Fair enough."
                    "He shakes off my hand and this time, I let him go. He huffs indignantly, and slouches off down the street."
                    "Grinning to myself a little, I return to my patrol."

    return

label l_swindle:
    "I'm walking through a market when..."
    unknown "My my, what a gorgeous selection you have here!"
    "I turn to the loud praise and watch."
    "A tall woman is leaning over the counter, with a merchant standing behind it, blushed red from ear to ear. The counter has treats, a mix of pastries, chocolates, and such, on display."
    woman2 "I would ever so much love to purchase one of these. Like this..."
    merchant "Th-that? Just five coppers..."
    "Moving to a slightly different angle makes it clear that the cut of her blouse affords him quite a sight of the woman's cleavage."
    "So it's like that..."
    
    menu:
        "Poor guy. Should I do something about it?"
        
        "Approach":
            "May as well."
            woman2 "Oh that would be wonderful, just let me..."
            "Ah, those do look nice."
            "When I cut in, the woman immediately straightens up."
            merchant "M-Miss?"
            "The guy's eyes move between us."
            "Oh my, it seems I forgot my coinpurse. I'll be going now. Tata."
            "With a stiff wave of her fingers, she quickly heads off."
            merchant "Haah... Good going, you scared off my customer."
            "She just said she didn't have any money."
            "He looks mildly displeased, but can't say anything in response."
            "With a shrug and a wave, I return to my patrol."
        
        "Keep watching":
            "Ehh, she's not doing anything illegal... yet..."
            woman2 "Oh that would be wonderful, just let me... Oh my, it seems I forgot my coinpurse."
            woman2 "Oh... W-well, maybe..."
            "Looking very uncomfortable, the man flounders in front of the woman."
            "If I'm going to step in, it has to be now..."
            
            menu:
                "Well, do you?"
                
                "Approach":
                    "I've seen enough."
                    "Walking quickly forward, I thump a hand down on the woman's shoulder, and she shoots back upright instantly."
                    "Miss, if you have no money to pay for things, I think it's best if you move along."
                    woman2 "Of-of course, constable."
                    "The woman flees quickly into the crowd."
                    "Ehh, it's not like tricking the guy into giving her some chocolates is illegal, but still..."
                    merchant "Aww..."
                    "I eye him, and he looks disappointed by the woman's departure."
                    "He hasn't even realized he was being swindled, has he?"
                    "Have a nice day."
                    "With a subtle shake of my head, I leave the foolish merchant behind, and return to my patrol."
                "Let it go":
                    "Ehh, it's not like tricking the guy into giving her some chocolates is illegal. If she swindles some chocolates out of him, maybe he'll learn a lesson."
                    "With a shrug of my shoulders, I leave the foolish merchant to his fate and return to my patrol."
        
        "Let it go":
            "Ehh, it's not like tricking the guy into giving her some chocolates is illegal. If she swindles some chocolates out of him, maybe he'll learn a lesson."
            "With a shrug of my shoulders, I leave the foolish merchant to his fate and return to my patrol."
    return
