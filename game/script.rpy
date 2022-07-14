# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define y = Character("You")
define t = Character("Tom")
define un = Character("???")
define teach = Character("Ms Sneezer")
define h = Character("Henry")
define l = Character("Leslie")
define b = Character("Billy")
define r = Character("Rob")
define j = Character("Jake")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music 'ghost.mp3'

    # These display lines of dialogue.

    un "Hey you!"
    show tom happy
    t "Nice to see you!"

    t "Have you done your Homework for today?"
    

    menu:

        "Yes, I did.":
            jump choice1_yes

        "No, I didn't bother.":
            jump choice1_no

        "Crap, I forgot about them!":
            jump choice1_forgor

    label choice1_yes:

        $ menu_flag = True
        t "Oh that's neat, I'm sure you're okay with me yoinking them for a couple minutes to copy them."
        jump choice1_done

    label choice1_forgor:
            $ menu_flag = True
            t "Haha that's the Friend I have, c'mon let's ask someone to copy the homework from."
            jump choice1_done

    label choice1_no:

        $ menu_flag = False
        show tom sad
        t "Geez...you should start studying or else you will have to repeat this year. Don't let me alone, man."

        jump choice1_done

    label choice1_done:

    t "Oh shoot, Ms. Sneez' is coming! We should go back to our seats."
    show tom happy at left
    hide tom
    show teach happy at right
    teach "Sit down everyone, I have an announcement to make. Today we are getting a new transfer student."
    show teach happy:
        xalign 0.5
        yalign 1.0
    show henry sad at right
    teach "Please go ahead and introduce yourself."
    
    un "Y-Yeah.. O-Okay.."
    show henry sad:
        xalign 0.5
        yalign 1.0
    hide teach
    un "*takes a deep breath*{p} H-He-Hello, my name is Henry and I just moved to my Mother's place."

    un "(What is wrong with this guy?...)"
    un "(...I think he has a stutter...)"
    un "(...and a bad one on top of that...)"
    show teach happy at left
    teach "Alright thank you Henry. You can go ahead and take a seat now."
    show henry sad at right
    h "O-Okay..."
    h"(Oh no, my introduction was even worse than I anticipated)"
    hide teach happy
    hide henry
    show tom sad
    t "(...Ahh.. this isn't going to end well, that's for sure...)"
    hide tom


    scene black
    with Dissolve(1)
    "Later that same day..."
    scene bg classroom
    with Dissolve(1)

    show teach happy
    teach "Leslie would you please hand these quiz sheets out?" 
     
    show leslie happy
    show teach happy at right
    l "Yes."
    hide leslie
    teach "Everyone, fill out the quiz until I am back."
    hide teach
    show tom sad
    t "And again we gotta do to stuff on our own..." 
    t "Why is Ms. Sneez even a teacher if she doesn't teach?"
   
    hide tom

    show billy happy
    b "HEY YOU!"
    b "HELLO!!!"
    show billy angry
    b "IM TALKING TO YOU!"
   
    hide billy
    show leslie angry
    l "Billy, stop screaming!"
    l "Im trying to concentrate on my Quiz so please keep it down."
    show leslie angry
    show billy angry at left
    b "Mind your own business Leslie. I have to to talk to Mr. New Guy here."
    show billy happy at left
    b "But it seems that he is deaf on top of having a huge stutter."
    b "Isn`t that right Deafy?"
    hide leslie
    show henry sad
    h "I-It's Henry. C-Call me Henry"
    show billy angry at left

    b "It's still me who gets to decied on how I call you."
    h "..."
   
    show billy happy:
            xalign 0.30
            yalign 1.0

    "Billy wraps his Arm around Henry's Shoulders"
    
    show henry sad
    b "Do you mind helping out a friend with his quiz?"
    "Billy snatches Henry's quiz sheet right out of his hands"

    show billy happy:
        xalign 0.25
        yalign 1.0
    b "Yes... I see... You are a smart one, aren't you?"
    b "I will borrow this if you don't mind"
    hide billy
    hide henry

    show tom sad

    t "It's his first day and Billy is already picking on the New Guy."
    show tom happy
    t "Glad that it's not us getting picked on by Billy, right?"

    menu:

        "True":
            jump choice2_1

        "I feel sorry for him.":
            jump choice2_2





       
    label choice2_1:
        show tom angry
        t "I guess thats what he gets after making himself such a clown in front of the class."
        jump choice2_done


    label choice2_2:
        show tom sad
        t "I mean, it's not like that i don't. I just don't want to get dragged into this mess."
        t"Let's just let this solve itself."

        jump choice2_done

    label choice2_done:

    hide tom

    scene black
    with Dissolve(1)
    "Class for today has ended"
    scene bg hallway  # DER HINTERGRUND MUSS NOCH HINZUGEFÜGT WERDEN
    with Dissolve(1)


    play music 'ghost.mp3' # ANDERE AFTER CLASS MUSIK MUSS HIER LAUFEN

    # These display lines of dialogue.
    show tom sad at left
    t "Puh... Watching Billy pick on the new guy on his first day was really nerve wracking."


    t "Look, over there. Henry is trying to sneak out of the class."
    show henry sad at right
    t "Yo Henry, there is no need for you to-"

    show billy happy
    b "So there you are Henry!"

    show billy happy:
        xalign 0.75
        yalign 1.0
    b "I was already looking for you."
    #hide tom
    h"..."

    b "Did you really think you can sneak out that easily?"
    
    h"....."

    b "Thank's to Tom I have finally found you."
    b "Now then. There is a ritual at our school for every new student that joins our class."

    t "Hmm? What is he talking about?"

    b "Today you gotta show us how strong you are. Let's go outside. The yard behind the Gym should be good."

    h "Wait, do I really have to..."
  
    b "Rob, Jake, drag him out!"

    r "Sure thing."
    show henry sad:
        xalign 1.1
        yalign 1.0
    j "Yeah, there is no escape for you, punk."
    show henry sad:
        xalign 1.2
        yalign 1.0
    h "Please, someone..."

    menu:

        "Step in":
            jump choice3_stepin

        "Follow them outside":
            jump choice3_followthem

        "Ignore them":
            jump choice3_ignorethem

    label choice3_stepin:

        $ menu_flag = True
        y "Hold it you guys! Leave him alone, he has no business with you. So stop pushing him around!"
        show billy angry
        b "Oh my, looks like someone is looking for trouble. You better look after yourself, idiot."
        
        "Billy pushes you back"
    
        r "If you want some too, then come outside. I will make you regret interfering us."
        j "Yeah, you stupid egghead! Don't mess with us!"

        "Billy, Rob and Jake leave the building and drag Henry with them"
        hide billy
        hide henry
        t "Oh no! Now he is really gonna be beaten up."
        t "I haven't seen Billy so angry in a long time."
        t "Please don't follow them. They will beat you up aswell. I'm sure of it."

        menu:

            "Go after them":
                jump choice3_followthem

            "Don't go after them":
                jump choice3_ignorethem

    label choice3_followthem:

        t "You are really doing this? I can't believe you wouldn't listen to me."

        scene black
        with Dissolve(1)
        "You leave the building and follow them outside"
        scene bg outside  # DER HINTERGRUND MUSS NOCH HINZUGEFÜGT WERDEN
        with Dissolve(1)

        play music 'ghost.mp3' # ANDERE MUSIK

        "You are looking behind the gym for Billy and the others."
        show billy happy:
            xalign 0.3
            yalign 1.0
        show henry sad:
            xalign 0.5
            yalign 1.0
        b "So then, what do you think about me?"

        h "What do you mean? Please let me go!"

        b "I asked you a question, now answer it!"
        show billy happy:
            xalign 0.4
            yalign 1.0
        "Billy punches Henry in the belly"
        show henry sad:
            xalign 0.7
            yalign 1.5
        h "OUUUUCHHH!!!!!!!!"
        "Henry is falling on his knees."
        "He is in alot of pain, he can't stand anymore."

        b "NOW THEN AM I THE STRONGEST HERE OR WHAT?!!"
        
        h"Y-Yes... You are..."
        show billy angry
        b "OF COURSE I AM!"
        b "You are nothing! Just look at yourself!"
        b "I hate people like you! Weak and miserable!"

        j "Guys someone is watching us!"

        b "You are off the hook for now. But don't you dare not showing up tomorrow!"
        hide billy
        "As quickly as the beat Henry up, as fast they left the Scene again."

        menu:

            "Help Henry":
                jump choice3_help

            "Leave him be":
                jump choice3_leavehim

        label choice3_help:

        y "Hey are you ok?"
        show henry sad:
            xalign 0.7
            yalign 1.0
        h "No..."
        y "How can I help you?"
        h "...."

        y "Let me get a teacher, they know what to do!"
        hide henry
        "You are looking for a teacher."
        show teach happy
        "You find Ms. Sneezer and tell her everything that happened and that Henry needs help."
        teach "Alright thank you. I can take care of it now. But leave him some room, would you?"
        jump choice3_done
        hide teach

        label choice3_leavehim:
            "You leave the scene and pretend like you didn't see what happened."
            jump choice3_done


    label choice3_ignorethem:
        show tom happy
        t "It's really nothing we should get involved in. Either Henry can handel it by himself or a teacher will help him." 
        t "But i guess that's just how Billy is."  

        jump choice3_done    
    
    label choice3_done:

    # AFTER SCHOOL AB HIER
    # HIER KOMMT DAS CYBERMOBBING
    


    show tom happy




    "To be continued"

    # This ends the game.

    return
