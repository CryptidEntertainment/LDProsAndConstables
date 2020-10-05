define cap = Character("Captain Louis Sirr")
# just in case
define cap_unknown = Character("Captain Louis Sirr")
define con_unknown = Character("Merchant")
define con = Character("Magic Mushrooms Merchant")
define guard = Character("Guard")
define merchant = Character("Merchant")
define peasant = Character("Peasant")
define thief = Character("Thief")
define unknown = Character("???")
define woman = Character("Woman")
define woman2 = Character("Woman")
define woman3 = Character("Woman")
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

default THIEVES_GUILD = "[THE THIEVES' GUILD]"

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
            
            you "Well, shit."
            
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
    you "Well. Today is Monday, and it's the beginning of another work day."
    you "I should get ready to work."
    
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

    #call l_morning
    
    #"A couple hours pass, and the sun is a little bit past overhead now. It beats warmly down on my tabard."
    #"I can hear the sound of chainmail approaching me. The next Constable should be coming for the afternoon shift."
    #"He give me a quick nod as he reaches me, and I take off to go to my afternoon assignment."
    #"The sounds of profit - that is, shouting and announcements and haggling - get louder as I approach the marketplace."
    #"I hope to myself that nothing terrible happens today."
    #"Something always happens, but I just hope it isn't too bad."
    
    #call l_afternoon
    
    #"The air begins to cool again as the sky darkens. My shift should be over about now."
    #"Time to report to Captain Sirr about the day."
    #"I walk back into the barracks, and find the Captain in his quarters."
    #"Captain Sirr: You're back safe and sound. What happened today?"
    
    #call l_night
    
    #"The air begins to cool again as the sky darkens. My shift should be over about now."
    #"I sigh, and head back to the barracks."
    #"And I do the same thing as I do, every night - take off my armor, hang up my tabard, and take out the oil and rag to clean them."
    #"My equipment is dusty. Walking the dirt roads all day will do that to them."
    #"After a while of polishing and cleaning, it's time to sleep. I lie down on my cot, and pull the woolen blanket over me."
    #"Eventually, my eyes turn heavy and the room goes dark."
    
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

label l_scene_pickpocket:
    "I'm crossing a street when a certain person moving in the crowd catches my eye with the way they're moving."
    "I watch close. He moves up behind a woman, then rushes forward, jostling past her and using the distraction to cut away her coin purse."
    
    menu:
        "What should I do?"
        
        "Ignore it":
            "Damn it, I really don't feel like dealing with thieves right now."
            "Turning my back on the scene, I let it pass and continue my patrol."
            "Must be one of [THIEVES_GUILD]. Just let him pass..."
            "Pretending not to notice, I continue my patrol."
        
        "Approach the man":
            "I give it some time, keeping my distance as I follow the thief. He's on guard for a minute before he calms down, and I'm able to get closer without him noticing."
            "Moving in behind him, I keep quiet until I'm right on him, and grab his arm hard."
            thief "What?!"
            "He spins back. When he sees me, he struggles, but my grip is solid, he isn't getting away from me that easily."
            you "I saw you rob that woman."
            "A grin breaks over his face, both mocking and worried at once."
            thief "Yeah? And what're you gonna do about it?"
            
            menu:
                "Good question. What {i}am{/i} I going to do about it?"
                
                "Make him give the money back":
                    you "You're giving that money back, and then you're going to jail."
                    "His grin widens."
                    thief "How about option three?"
                    "With his free hand, he tosses the coin purse up into the air."
                    you "Shit!"
                    "I stagger backward, diving and falling flat on my back as I barely catch the bag to keep it from spilling its contents all over the ground."
                    you "Ugh. He got away."
                    "By the time I've recovered and made it back to my feet, the thief is long gone."
                    you "At least I got the money back."
                    "After backtracking to where the woman was pickpocketed, I have to search the nearby areas before I find her."
                    you "Excuse me, Miss."
                    woman "Yes, constable?"
                    you "You were pickpocketed earlier. I recovered your coin purse for you."
                    "As soon as I show her the bag, her hand goes to her waist, searching for the missing purse."
                    woman "Oh, oh my! I didn't even..."
                    woman "Thank you so much!"
                    you "Just doing my job."
                    "I hand back her coin purse, and she quickly fastens it back in place, before seeing me off."
                    "As I'm walking away, a random thought comes back to mind."
                    you "Did he say \"option three?\" I never gave him an option two..."
                    "Shake my head, laughing a little to myself as I return to my patrol."
                
                "Don't bother":
                    you "Nothing."
                    thief "Huh?"
                    you "I'm not going to do anything about it."
                    "I crack a grin."
                    you "I'm going to let you go, and you’re going to remember it."
                    you "You're going to owe me one. Remember that."
                    "The man’s expression turns sour."
                    thief "Fair enough."
                    "He shakes off my hand and this time, I let him go. He huffs indignantly, and slouches off down the street."
                    "Grinning to myself a little, I return to my patrol."

    return

label l_scene_swindle:
    "I'm walking through a market when..."
    unknown "My my, what a gorgeous selection you have here!"
    "I turn to the loud praise and watch."
    "A tall woman is leaning over the counter, with a merchant standing behind it, blushed red from ear to ear. The counter has treats, a mix of pastries, chocolates, and such, on display."
    woman2 "I would ever so much love to purchase one of these. Like this..."
    merchant "Th-that? Just five coppers..."
    "Moving to a slightly different angle makes it clear that the cut of her blouse affords him quite a sight of the woman's cleavage."
    you "So it's like that..."
    
    menu:
        "Poor guy. Should I do something about it?"
        
        "Approach":
            "May as well."
            woman2 "Oh that would be wonderful, just let me..."
            you "Ah, those do look nice."
            "When I cut in, the woman immediately straightens up."
            merchant "M-Miss?"
            "The guy's eyes move between us."
            woman2 "Oh my, it seems I forgot my coinpurse. I'll be going now. Tata."
            "With a stiff wave of her fingers, she quickly heads off."
            merchant "Haah... Good going, you scared off my customer."
            you "She just said she didn't have any money."
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
                    you "I've seen enough."
                    "Walking quickly forward, I thump a hand down on the woman's shoulder, and she shoots back upright instantly."
                    you "Miss, if you have no money to pay for things, I think it's best if you move along."
                    woman2 "Of-of course, constable."
                    "The woman flees quickly into the crowd."
                    "It's not like tricking the guy into giving her some chocolates is illegal, but still..."
                    merchant "Aww..."
                    "I eye him, and he looks disappointed by the woman's departure."
                    "He hasn't even realized he was being swindled, has he?"
                    you "Have a nice day."
                    "With a subtle shake of my head, I leave the foolish merchant behind, and return to my patrol."
                "Let it go":
                    you "Ehh, it's not like tricking the guy into giving her some chocolates is illegal. If she swindles some chocolates out of him, maybe he'll learn a lesson."
                    "With a shrug of my shoulders, I leave the foolish merchant to his fate and return to my patrol."
        
        "Let it go":
            you "Ehh, it's not like tricking the guy into giving her some chocolates is illegal. If she swindles some chocolates out of him, maybe he'll learn a lesson."
            "With a shrug of my shoulders, I leave the foolish merchant to his fate and return to my patrol."
    return

label l_scene_mushrooms:
    "As I’m walking through the marketplace, I hear a voice begin shouting excitedly over all of the others. I walk over to the commotion."
    con "Buy Arcane Mushrooms today! They’ll solve any problem, guaranteed! Buy 'em today!"
    "I don’t recognise this merchant… and what the hell is it that he’s peddling?"
    "A small crowd has already gathered around this man."
    
    menu:
        "Should I do something about it?"
        
        "Approach":
            you "Move aside, move aside, constable coming through."
            "I should at least figure out what’s going on. I make my way past a couple people and walk up to the merchant."
            "There are many types of mushrooms on his stand, all shapes and sizes and colors."
            "He’s smiling. He almost seems too happy to see me walking up to his stand."
            you "I don’t think I’ve even seen you around before. You new in this market?"
            con "Why yes, because I’m a travelling merchant! I started my mushrooming journey a few years ago, all the way back in the land of—"
            you "I don’t need to hear your life’s story. Tell me more about what you’re selling."
            con "Why, they’re Arcane Mushrooms! They’ll fix any and every problem in your life! There’s a mushroom for every occasion, and they’re simply magical!"
            "I don’t know how much I trust this man, and I know nothing about his product."
            
            menu:
                "What's the logical course of action?"
                
                "Question him further":
                    you "Tell me more about what these mushrooms can specifically do."
                    con "Why, they alleviate headaches and stomachaches and can cure any sickness or physical ill!"
                    con "They can bulk up your muscles, make you more flexible, or make you think twice as fast as you do right now!"
                    you "How do you know that they work? Have you eaten all of these before?"
                    "A bead of sweat begins to drip down the merchant’s forehead."
                    con "Why, well the phrase amongst us dealers is to not get hi- I mean, don’t deny your whole supply to your customers!"
                    con "I’d lose a lot of profit if I did that! Imagine if a butcher ate half of every steak that he had to peddle."
                    you "Certainly they’re all safe to eat, right?"
                    con "Of course they’re all safe! I’ve been selling them for years without incident!"
                    con "Not a single soul has ever died because of my mushrooms and come to me complaining about it."
                    "Something feels very suspicious about this man and the way he answers my questions."
                    
                    menu:
                        "What should I do about this?"
                        
                        "Kick him out of town":
                            "I can’t just let this man scam our village out of money and possibly poison our peasantry."
                            you "Alright. Here’s what’s going to happen. You’re going to pack up your little stand here, and keep moving to another town."
                            con "What? Why! I haven’t done anything wrong!"
                            peasant "Oi, wait, I din’t get to buy any anyfin’ yet!"
        "Bring up the issue to the Captain":
            pass
        "Let the man sell his goods":
            pass
    return

label l_scene_murder:
    "I’m stationed at a gate when…"
    woman3 "EEEEIIIIIIAAAAAAAAA!!!!!!"
    "Everyone jumps at the piercing scream."
    guard "That was really close."
    
    menu:
        "Do you go to investigate?"
            "I should check that out!":
                guard "Wait! Leave it for the patrols."
                you "We’re the closest, and it sounded bad!"
                "Before anyone can argue further, I rush away from the gate, toward the sound of the scream."
                "It’s just a couple blocks, and I’m there in no time."
                you "Oh, shit!"
                "As soon as the scene comes into sight, my blood runs cold."
                "There are a few people scattered about watching, and a woman collapsing, a pool of deep red blood already forming beneath her."
                "I barely spot the glint of metal and the flick of blood as the perpetrator flees, turning a corner and disappearing."
                you "Guard! Move aside!"
                "My voice clears the crowd so I can slide to the woman’s side. One look shows she’s been stabbed badly in the stomach."
                "One hand immediately applies pressure to the wound while I dig through my gear with the other for my medical supplies."
                woman3 "Why? I didn’t… I didn’t do anything wrong…"
                you "Don’t speak, just stay still. I’m here to help."
                "She goes quiet, her eyes slowly losing focus."
                "I pull out some supplies. They’re not much, but it’ll help. It’s hard to say for sure, but I think I’ve seen enough wounds to know that a stab in this spot won’t hit anything vital."
                "Besides the severe bleeding, I don’t see any other signs of organ damage, or so I hope. As fast as I can, I use my supplies to treat the wound, then bandage it as well as I can."
                you "Don’t worry, you’ll be alright. Everything will be fine..."
                "I keep talking to her as I work, even though she’s slowly losing consciousness from the blood loss."
                "Then I finish. It looks like I’ve stopped most of the immediate bleeding, but her eyes are barely open anymore, and her head lolls limply to the side."
                you "I hope you make it…"
                guard "Guards coming through!"
                "I stand to meet the approaching guards."
                guard "What are you doing here?"
                you "I was closest to the scene, over at the gate. I treated her wounds, but she still needs real medical attention."
                "The guards all inspect the half-conscious woman uncertainly."
                guard "Sure… We’ll deal with it from here, get back to your post!"
                you "Of course."
                "With a quick salute, I leave the scene to the patrol guards. I know I shouldn’t have abandoned my post, but that woman would have died if I hadn’t gotten there as soon as I did."
                "Thinking that, I return to my post."
            "I have to stay at my post"
                you "We have to stay here. This is our post."
                guard "Obviously. Let the patrol guards deal with it."
                "We all nod, and continue manning the gate."
    return
