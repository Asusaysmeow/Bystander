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
    
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music 'ghost.mp3'

    # These display lines of dialogue.

    un "Hey you!"
    show tom happy
    t "Nice to see you!"

    t "Have you done your Homework for today?"
    show tom happy at left

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
            t "Haha that's the Friend I have, c'mon let's ask someone to copy the Homework from."
            jump choice1_done

    label choice1_no:

        $ menu_flag = False

        t "Geez...you should start studying or else you will have to repeat this year. Don't let me alone, man."

        jump choice1_done

    label choice1_done:

    t "Oh shoot, Ms. Sneez' is arriving! We should go back to our seats."
    show tom happy at left
    hide tom

    teach "Sit down everyone, I have an announcement to make. Today we are getting a new Student."
    teach "*Yawn* Please go ahead and introduce yourself."
    
    show henry sad at right
    un "Y-Yeah.. O-Okay.."
    show henry sad:
        xalign 0.5
        yalign 1.0
    un "*takes a deep breath* H-He-Hello, my name is Henry and I just moved to my Mother's place."

    "Girl voice" "Where did you live before?"  
    h "I-I lived with my Dad but he h-has to w-wo-work abroad now." 

    un "(...Haha, look at him, he is about to cry, what a weakling....)"
    #show teach happy
    teach "Stop talking everyone, we are about to start class. Go sit down Hans"
    #show henry sad
    h "O-Okay..."
    h"(..My Name is Henry, not Hans...)"
    #hide teach happy
    #hide henry sad
    t "(...Ahh.. this isn't going to end well, that's for sure...)"
    #hide tom sad
    "Some time passes.."
    teach "Okay, Leslie hand these out. Fill the quiz until I am back.  This is your assignment for today."
    l "Yes."

    #show tom happy
    t "And again we get do to stuff on our own.. why is Ms. Sneez' even a teacher if she doesn't teach."

    b "HEY HANS!"
    b "HEEEEEEEEY!!!"
    b "HAAAANS I AM TALKING TO YOU!!"
    l "Billy, stop screaming!"
    l "Im trying to concentrate on my Quiz so please keep it down."
    l"Also, his name is Henry and not Hans. "
 
    "Boy voice" "Haha she is right Billy, are that dumb, that you forget his name even thought it isn't even 10 mins past him telling his name to us."
    b "SHUT THE FUCK UP"
    b "I called him like that on purpose, because Ms Sneez' couldnt even listen to him talk. What a disgrace. "
    un "Yeah you're right, he didn't even correct her."
    un "Might aswell be his Name if he didnt respond, haha."
    b "Yes, you get it! Hans, if you have a problem with how I call you, we can solve that on the basketball field later."
    h "A-Ah.. C-Call me w-whatever y-you want.."
    b "Hahah, see Leslie?"
    b "he doesn't have a problem with me calling him Hans!"
    l "*rolls her eyes* yeah yeah.."
    l "(...only because you threatened him...)"
    "Billy wraps his Arm around Henry's Shoulders"
    b "So Hans, are you going to help your first Friend out and give me your Quiz sheet?"
    h "..."
    b "Hahahah, neat! Thanks Hans!"

    show tom sad

    t "Billy is already teasing Hans, that's so mean.."

    menu:

        "His name is Henry, not Hans.":
            jump choice2_yes

        "Yes, poor Hans.":
            jump choice2_no





       
    label choice2_yes:

       # $ menu_flag = True
        t "Oh you're right, im sorry! Billy calling him Hans all the time made me forget."
        jump choice2_done


    label choice2_no:

       # $ menu_flag = False

        t "I don't want to get dragged into that mess."

        jump choice2_done

    label choice2_done:

    "Nothing yet"

    # This ends the game.

    return
