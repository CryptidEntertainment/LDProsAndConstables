define cap = Character("Captain Louis Sirr")
# just in case
define cap_unknown = Character("Captain Louis Sirr")
define child = Character("Child")
define con_unknown = Character("Merchant")
define con = Character("Magic Mushrooms Merchant")
define dave = Character("Dave")
define drunk_unknown = Character("???")
define drunk = Character("Drunk")
define guard = Character("Guard")
define man = Character("Man")
define merchant = Character("Merchant")
define peasant = Character("Peasant")
define thief = Character("Thief")
define unknown = Character("???")
define woman = Character("Woman")
define woman2 = Character("Woman")
define woman3 = Character("Woman")
define woman4 = Character("Woman")
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
default player_pronoun_informal = "chap"
default player_pronoun_honorific = "Overlord"

default day_index = 0
default day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
default scenes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
renpy.random.shuffle(scenes)

image mom = "chicken.png"
image shit = "shit.png"
image sir = "sir.png"
image hair = "hair.png"
image urchin = "derp.png"
image merchant = "hat.png"
image drunkard = "beer.png"

default THIEVES_GUILD = "[THE THIEVES' GUILD]"
default DAYS_TOTAL = 6

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
            $ player_pronoun_informal = "old chap"
            $ player_pronoun_honorific = "my good"
        "He/him":
            $ player_pronoun_subject = "he"
            $ player_pronoun_object = "him"
            $ player_pronoun_possessive = "his"
            $ player_pronoun_verb = "is"
            $ player_pronoun_cap_subject = "He"
            $ player_pronoun_cap_object = "Him"
            $ player_pronoun_cap_possessive = "His"
            $ player_pronoun_informal = "sonny"
            $ player_pronoun_honorific = "Mister"
        "She/her":
            $ player_pronoun_subject = "she"
            $ player_pronoun_object = "her"
            $ player_pronoun_possessive = "her"
            $ player_pronoun_verb = "is"
            $ player_pronoun_cap_subject = "She"
            $ player_pronoun_cap_object = "Her"
            $ player_pronoun_cap_possessive = "Her"
            $ player_pronoun_informal = "lassie"
            $ player_pronoun_honorific = "Missus"
    
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
    $ day_index_sub = DAYS_TOTAL - day_index
    $ day_index_name = day_names[day_index]
    
    "It's the crack of dawn, and the sun has begun rising."
    "Today is [day_index_name], with [day_index_sub] days until the end of the week."
    "Time to don my chainmail and get ready for work."
    menu:
        "Grab your mace and get out there":
            pass

    "The morning air is still cold when I leave the barracks. The morning dew wets my boots."
    "I walk through the dirt roads until I get to my assigned post."
    "The sun is just over the horizon, now, and my shift begins."
    "Let's see what happens today..."
    
    if scenes[day_index] == 0:
        jump l_scene_change
    elif scenes[day_index] == 1:
        jump l_scene_drunk
    elif scenes[day_index] == 2:
        jump l_scene_drunk_nuisance
    elif scenes[day_index] == 3:
        jump l_scene_fight
    elif scenes[day_index] == 1:
        jump l_scene_murder
    elif scenes[day_index] == 5:
        jump l_scene_mushrooms
    elif scenes[day_index] == 6:
        jump l_scene_pickpocket
    elif scenes[day_index] == 7:
        jump l_scene_swindle
    elif scenes[day_index] == 8:
        jump l_scene_chicken
    
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
    
    if day_index < DAYS_TOTAL:
        jump l_cycle
    
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
                    you "I'm going to let you go, and you're going to remember it."
                    you "You're going to owe me one. Remember that."
                    "The man's expression turns sour."
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
    "As I'm walking through the marketplace, I hear a voice begin shouting excitedly over all of the others. I walk over to the commotion."
    con "Buy Arcane Mushrooms today! They'll solve any problem, guaranteed! Buy 'em today!"
    "I don't recognise this merchant... and what the hell is it that he's peddling?"
    "A small crowd has already gathered around this man."
    
    menu:
        "Should I do something about it?"
        
        "Approach":
            you "Move aside, move aside, constable coming through."
            "I should at least figure out what's going on. I make my way past a couple people and walk up to the merchant."
            "There are many types of mushrooms on his stand, all shapes and sizes and colors."
            "He's smiling. He almost seems too happy to see me walking up to his stand."
            you "I don't think I've even seen you around before. You new in this market?"
            con "Why yes, because I'm a travelling merchant! I started my mushrooming journey a few years ago, all the way back in the land of—"
            you "I don't need to hear your life's story. Tell me more about what you're selling."
            con "Why, they're Arcane Mushrooms! They'll fix any and every problem in your life! There's a mushroom for every occasion, and they're simply magical!"
            "I don't know how much I trust this man, and I know nothing about his product."
            
            menu:
                "What's the logical course of action?"
                
                "Question him further":
                    you "Tell me more about what these mushrooms can specifically do."
                    con "Why, they alleviate headaches and stomachaches and can cure any sickness or physical ill!"
                    con "They can bulk up your muscles, make you more flexible, or make you think twice as fast as you do right now!"
                    you "How do you know that they work? Have you eaten all of these before?"
                    "A bead of sweat begins to drip down the merchant's forehead."
                    con "Why, well the phrase amongst us dealers is to not get hi- I mean, don't deny your whole supply to your customers!"
                    con "I'd lose a lot of profit if I did that! Imagine if a butcher ate half of every steak that he had to peddle."
                    you "Certainly they're all safe to eat, right?"
                    con "Of course they're all safe! I've been selling them for years without incident!"
                    con "Not a single soul has ever died because of my mushrooms and come to me complaining about it."
                    "Something feels very suspicious about this man and the way he answers my questions."
                    
                    menu:
                        "What should I do about this?"
                        
                        "Kick him out of town":
                            "I can't just let this man scam our village out of money and possibly poison our peasantry."
                            you "Alright. Here's what's going to happen. You're going to pack up your little stand here, and keep moving to another town."
                            con "What? Why! I haven't done anything wrong!"
                            peasant "Oi, wait, I din't get to buy any anyfin' yet!"
        "Bring up the issue to the Captain":
            pass
        "Let the man sell his goods":
            pass
    return

label l_scene_murder:
    "I'm stationed at a gate when..."
    woman3 "EEEEIIIIIIAAAAAAAAA!!!!!!"
    "Everyone jumps at the piercing scream."
    guard "That was really close."
    
    menu:
        "Do you go to investigate?"
            "I should check that out!":
                guard "Wait! Leave it for the patrols."
                you "We're the closest, and it sounded bad!"
                "Before anyone can argue further, I rush away from the gate, toward the sound of the scream."
                "It's just a couple blocks, and I'm there in no time."
                you "Oh, shit!"
                "As soon as the scene comes into sight, my blood runs cold."
                "There are a few people scattered about watching, and a woman collapsing, a pool of deep red blood already forming beneath her."
                "I barely spot the glint of metal and the flick of blood as the perpetrator flees, turning a corner and disappearing."
                you "Guard! Move aside!"
                "My voice clears the crowd so I can slide to the woman's side. One look shows she's been stabbed badly in the stomach."
                "One hand immediately applies pressure to the wound while I dig through my gear with the other for my medical supplies."
                woman3 "Why? I didn't... I didn't do anything wrong..."
                you "Don't speak, just stay still. I'm here to help."
                "She goes quiet, her eyes slowly losing focus."
                "I pull out some supplies. They're not much, but it'll help. It's hard to say for sure, but I think I've seen enough wounds to know that a stab in this spot won't hit anything vital."
                "Besides the severe bleeding, I don't see any other signs of organ damage, or so I hope. As fast as I can, I use my supplies to treat the wound, then bandage it as well as I can."
                you "Don't worry, you'll be alright. Everything will be fine..."
                "I keep talking to her as I work, even though she's slowly losing consciousness from the blood loss."
                "Then I finish. It looks like I've stopped most of the immediate bleeding, but her eyes are barely open anymore, and her head lolls limply to the side."
                you "I hope you make it..."
                guard "Guards coming through!"
                "I stand to meet the approaching guards."
                guard "What are you doing here?"
                you "I was closest to the scene, over at the gate. I treated her wounds, but she still needs real medical attention."
                "The guards all inspect the half-conscious woman uncertainly."
                guard "Sure... We'll deal with it from here, get back to your post!"
                you "Of course."
                "With a quick salute, I leave the scene to the patrol guards. I know I shouldn't have abandoned my post, but that woman would have died if I hadn't gotten there as soon as I did."
                "Thinking that, I return to my post."
            "I have to stay at my post"
                you "We have to stay here. This is our post."
                guard "Obviously. Let the patrol guards deal with it."
                "We all nod, and continue manning the gate."
    return

label l_scene_fight:
    "I'm walking through a crowded district when..."
    unknown "Argh!"
    "The cry draws my attention down an alley, before I know it, I've passed through, straight into a familiar scene."
    "One man lies unconscious, the other sitting on the ground, beaten and bruised."
    you "It must have been a fight. This guy obviously won."
    you "What happened here?"
    man "C-constable!"
    "As soon as he turns and sees me, his eyes go wide and afraid."
    man "W-we just got robbed! They knocked out my friend!"
    you "Robbed?"
    
    menu:
        "Do I go with it or...?"
        
        "Ask for details on thieves":
            you "Tell me about these thieves."
            man "Of course! There were three of them. They were all in black with these, these robes, and they just ran all up around us and attacked us."
            man "They beat us up and stole all our money."
            you "Does he really expect me to believe it was people in dark robes? Why not just say some hoodlums? At least that would be sort of believable."
        
        "Examine the other man":
            you "So, what about your friend here?"
            "I kneel down over the unconscious man and look him over. He's beaten and bruised, but it doesn't look life threatening."
            you "So, what's your buddy's name, here?"
            man "Him? Uhh, Jack. His name is Jack."
            you "What were you two doing? This isn't exactly the greatest place in town you know."
            man "Ahh, well, about that, we were, uhh..."
            you "Ok, come on. If you don't start telling the truth, I'm going to arrest you."
            "The man jolts, then his face falls."
            man "Alright, we were actually heading to my sister's house. He uhh..."
            "The man scratches his head and clears his throat."
            man "My sister might have been having an affair with him. If it was true, I would have thrown him a beating later. But I didn't yet! We really were just robbed!"
            "He waves his hands frantically as he tries to clarify."
            you "Hmm..."
            you "With a story that wild, I have no idea what to believe... Is he just making up something wild, or is he actually telling the truth?"
            you "Either way, he actually admitted that he already intended to attack the man later. That alone would be enough to lock him up, but if he's telling the truth, the guy might have it coming..."
            
            menu:
                "I turn to stare at the man, trying to make up my mind."
                
                "Jail him":
                    you "I'm taking you in."
                    "I grab him and haul him up to his feet."
                    man "W-what? Why?"
                    you "Either you're lying and you just attacked this man, or you're not, and you just admitted intent to attack him. Either way, you've broken the law."
                    "While speaking, I drag him after me. He struggles a little in my grip, but doesn't put his heart into it. Even if he did, he's not in any condition to provide real resistance."
                    "As we leave, I look back at the man on the ground, but he doesn't show any signs of waking up yet, and he's too large to carry."
                    you "I'll check on him later."
                    "While I pull the man over to the jail, he keeps his head down."
                    man "What about my sister...? What am I supposed to do...?"
                    "I shake my head and ignore him. Whatever his reasons, he's a criminal now."
                    "When we arrive at the jail, I pass him off to the guards there."
                    you "Can't be sure, he either attacked a man, or planned to attack him later."
                    guard "Alright, we'll take it from here."
                    "With a quick salute, I head back."
                    "I return to the spot where the unconscious man was, but he's gone when I arrive."
                    you "Huh, too bad."
                    "I'm disappointed that I couldn't get the full story from the other man, but there's nothing I can do about it now."
                    "Turning away, I return to my patrol."
                
                "Let him go":
                    you "Fine, fine. I'll believe your story. However..."
                    "I glower down at him on the ground."
                    you "You just admitted that you plan to attack this man later. Even if he has it coming to him, that is illegal."
                    "He shrinks back, lowering his head."
                    you "I'm going to let you off with a warning this time. No matter what he did with your sister, you can't just go around beating people."
                    you "If you want, you can consider getting robbed his recompense."
                    man "Y-yes, constable..."
                    you "Now come on, let's get you guys out of the street."
                    "After I give him a hand up from the ground, we work together to carry the unconscious man a few blocks further, to his supposed sister's house."
                    "I leave the men on the doorstep. He can barely keep the other upright as he leans against the door, but he manages."
                    man "Thank you, really."
                    "I wave him off, watching as he awkwardly fumbles through the door with the unconscious man. Indistinct voices come from inside, but I turn away and return to my patrol."
        
        "That's enough":
            you "Yeah, yeah, I've heard enough. I'm taking you in."
            "I grab him before he can react or try to run, and haul him up to his feet."
            man "W-what? Why?"
            you "If you're going to lie to my face, at least try to make it believable."
            "I sigh and drag him after me. He struggles, but he's not in any condition to provide real resistance."
            "I look back at the man on the ground, but he doesn't show any signs of waking up yet, and he's too large to carry."
            you "I'll check on him later."
            "After walking for a while, we arrive at the jail. I pass him off to the guards there."
            you "He attacked a man, then lied about it."
            guard "Alright, good job."
            "After just a few words and a quick salute, I head back."
            "I return to the spot where the unconscious man was, but he's gone when I arrive."
            you "Huh, guess he woke up. Would've been nice to find out what actually happened, but... oh well."
            "Shrugging it off, I return to my patrol."
        
        "Jail him for lying about knocking out the other man":
            you "Yeah, yeah, uh huh."
            "I grab the man and haul him up from the ground."
            man "Wh-what?"
            "He struggles in my grip, but he isn't in any condition to offer real resistance."
            you "You're coming with me."
            "When we arrive at the jail, I pass him off to the guards there."
            you "He attacked a man, then lied about it."
            guard "Alright, good job."
            "With just a couple words and a quick salute, I head back."
            "I return to the spot where the unconscious man was, but he's gone when I arrive."
            you "Gone, huh... Whatever."
            "Shrugging, I return to my patrol."
    return

label l_scene_change:
    "I'm on patrol when..."
    child "Hey Mister, hey Mister!"
    "A small street child runs up to me, grabbing my leg."
    child "Could you spare some change?"
    
    menu:
        "Can I do that?"
        
        "Refuse":
            you "Ugh, off me!"
            "I shake him off, scowling."
            you "Scram! Get out of here before I arrest you for disturbing the peace."
            child "Eep!"
            "He dashes away into the crowd."
            "I sigh, shaking my head, and return to my patrol."
        
        "Give him something":
            you "Sure, why not?"
            "I flip him a coin."
            child "Thanks a lot, Mister!"
            "With a smile on his face, he dashes away into the crowd."
            "I return to my patrol."
    return

label l_scene_chicken:
    "I'm put on duty guarding the jail, when..."
    unknown "Guards, guards!"
    "An exhausted looking woman runs up to me."
    woman "Please, please come help!"
    you "I could, but I'd be leaving my post."
    
    menu:
        "This could be a distraction..."
        
        "She needs help!":
            you "Of course!"
            "I dash after the woman as she runs away. We go a few blocks, arriving in front of a tree."
            woman4 "There, my baby is up there!"
            "She points up the tree and..."
            you "Is that a chicken?"
            "Up in the tree, there's a chicken, seemingly stuck."
            "All the tension about the woman who seemed to need help vanishes."
            you "Well, I'm already here..."
            "Thinking as much, I climb up into the branches and grab the chicken. It struggles a little, but I manage to get back down without too much trouble."
            you "Here's your... bird, ma'am."
            woman4 "Oh, thank you! Thank you so much."
            "Hugging the animal to her chest, she runs off."
            "Shaking my head, I return to my post."
        
        "This must be a distraction":
            you "Sorry ma'am, I can't leave my post."
            "I try not to show my skepticism in my response. If she's just a distraction, she's failed."
            "Without delay, she turns away and runs off."
            woman4 "Help, someone please help!"
            "Her shouts disappear into the street."
            "you I wonder if she really needs help with something...?"
            "Shrugging, I continue to stand guard."
    return

label l_scene_drunk:
    "While I'm on patrol..."
    drunk_unknown "Oya there, *hic*"
    "I turn and find a clearly drunk man approaching."
    drunk "How's its all shaking, (Sonny, Lassy, Yous)?"
    "I sigh."
    
    menu:
        "..."
        
        "Talk to him":
            you "What is it, old man?"
            drunk "Haha! Just a lookin a talka bit!"
            you "What about?"
            drunk "Oh, you know, *hic* life an' all da stuff whereabouts ya getting by..."
            "Grinning faintly at the man, I listen to him ramble for a bit. He doesn't get anywhere but he does vaguely recall a couple amusing stories before I give him a pat on the shoulder."
            you "Well, I have a patrol to return to, Have a nice day, sir."
            drunk "Youz too, [player_pronoun_honorific] constable, [player_pronoun_informal], haha."
            "He throws a drunken salute, as he staggers away."
            "I chuckle a bit, and return to my patrol."
        
        "Send him away":
            you "You're drunk, sir."
            drunk "You sure? I don't *hic* feel drunk!"
            you "Off with you now!"
            "I shoo him away. He grouches at me, but staggers off."
            "I roll my eyes, and return to my patrol."
    return

label l_scene_drunk_nuisance:
    "I hear drunken shouting and cheering. Rounding a corner to find it, I see a small gathering of peasants."
    "Each of their faces are rosy, and most of them have spills on their shirts. The smell of alcohol fills my nostrils."
    dave "Ha! And then the knave produced a dagger and advanced towards me, when I unsheathed mine rapier and laughed at him."
    dave "And we had a good bout of banter! \"Thine sword's looking a little short, sir!\""
    dave "He replied \"Ha! Ye've got yerself a big ol' blade, ye compensatin' fer anyfin?\""
    "By this time, I've walked all the way up to the group. I'm about to say something, when-"
    dave "Now hold, fellow friends, now who approaches our little gathering? Behold this [player_pronoun_informal], all dressed up in crimson and gold!"
    "He parts the gathering and points directly at me."
    dave "Pray tell, whomst art thou?"
    "you I'm a City Constable, friend. I just wanted all of you to-"
    dave "Constable? More like THINE MOMSTABLE! They allow anyone to be a guard these days, doth they not?"
    "The commoners chortle at the insult."
    you "You've got a lot of ale out in public, Dave. You know it's illegal to be drunk in public during the day, right?"
    "The clearly drunk peasants quiet up and look at Dave."
    dave "Dearest constable, you bastard, certainly thou wouldst understand that these bottles of booze art for my family?"
    dave "They are very thirsty, and I provide for them so they can drink."
    "The peasantry holler and laugh at this."
    
    menu:
        "Clearly, normal talk isn't going to work."
        
        "Insult him back":
            "My face turns into a sour scowl. I am fed up with these idiots right now."
            you "You're all in the wrong place, did you know?"
            "Dave, the drunk, theatrically feigns terror, mocking my words."
            dave "Oh, nay! Is the big, scary constable going to arrest all of us for jesting and being merry?"
            you "Pfft. The dung-covered peasant convention already left town yesterday. You should catch up before they get a new main attraction."
            dave "Oh, art thou mad, brother? A City Constable, resorting to mocking a drunk. Ha!"
            dave "I was right! Thou art nothing but a bastard with a chain coating and bastard filling."
            "The commoners continue shouting and I begin to feel my blood boil."
            you "Dave! I-"
            dave "Oh, feel not bad, Constable. Maybe thou just art not cut out to be... well, much of anything."
            dave "Thy mind art as strong as thine body- not at all!"
            "I've had enough. I have to get out of there before I do something to get me thrown into the jail cell."
            dave "Pray tell, mine fellow in a tabard of red and gold, that thou had not filled thine pants with a similar gold?"
            dave "Gaze upon the mighty Constable running away from some filthy peasants, retreating home to change his trousers!"
            "The peasants roar with laughter as I storm away, their voices slowly fading down the street."
        
        "Assert yourself":
            "I begin to shout and the inebriated idiots."
            you "Listen up! All of you need to go home. You're causing a ruckus, and I don't want to have to drag any of you away. Understand?"
            "The peasantry grumble, and some begin to pick up their stuff."
            dave "Constable, certainly we have not-"
            you "No, I'm not going to let you finish. Either you stop causing a scene in the street, or you-"
            dave "Mine good fellows, don't get let your spirits fall. For we shall continue our festivities at my abode! Tally-ho!"
            "The commoners cheer once more, as they stumble down the dirt paths out of the street."
    
    "Well, that takes care of that."
    return