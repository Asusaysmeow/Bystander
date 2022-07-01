# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define t = Character("Tom")
define un = Character("???")
define teach = Character("Ms Sneezer")
define h = Character("Henry")
define l = Character("Leslie")
define b = Character("Billy")
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
    "Some time passes.."
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
    h "I-It´s Henry. C-Call me Henry"
    show billy angry at left

    b "It´s still me who gets to decied on how I call you."
    h "..."
   
    show billy happy:
            xalign 0.30
            yalign 1.0

    "Billy wraps his Arm around Henry's Shoulders"
    
    show henry sad
    b "Do you mind helping out a friend with his quiz?"
    "Billy snatches Henry´s quiz sheet right out of his hands"

    show billy happy:
        xalign 0.25
        yalign 1.0
    b "Yes... I see... You are a smart one, aren´t you?"
    b "I will borrow this if you don´t mind"
    hide billy
    hide henry

    show tom sad

    t "It´s his first day and Billy is already picking on the New Guy."
    show tom happy
    t "Glad that it´s not us getting picked on by Billy, right?"

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
        t "I mean, it´s not like that i don´t. I just don´t want to get dragged into this mess."
        t"Let´s just let this solve itself."

        jump choice2_done

    label choice2_done:

    hide tom

    "To be continued"

    # This ends the game.

    return
