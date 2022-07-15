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


    play music 'ruins.mp3' # ANDERE AFTER CLASS MUSIK MUSS HIER LAUFEN

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
    show rob happy
    r "Sure thing."
    
    show henry sad:
        xalign 1.1
        yalign 1.0

    show jake happy:
        xalign 0.35
        yalign 1.0
    j "Yeah, there is no escape for you, punk."

    show rob happy:
        xalign 0.85
        yalign 1.0
    show jake happy:
        xalign 1.0
        yalign 1.0
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

            play music 'tension.mp3' # ANDERE MUSIK

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
            play sound 'slap.ogg'
            h "OUUUUCHHH!!!!!!!!"
            "Henry is falling on his knees."
            "He is in alot of pain, he can't stand anymore."

            b "NOW THEN AM I THE STRONGEST HERE OR WHAT?!!"
            
            h"Y-Yes... You are..."
            show billy angry
            b "OF COURSE I AM!"
            b "You are nothing! Just look at yourself!"
            b "I hate people like you! Weak and miserable!"
            show jake happy at left
            j "Guys someone is watching us!"

            b "You are off the hook for now. But don't you dare not showing up tomorrow!"
            hide billy
            hide jake
            "As quickly as they beat Henry up, as fast they left the Scene again."

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

    
    # HIER KOMMT DAS CYBERMOBBING
    


  


    scene bg bedroom
    play music 'reunited.mp3'
  
    "Phone is ringing nonstop"
    play sound 'ring.mp3'
    "*Checks his messages*"
    "Henry joined the chatroom of the class"
    

    l "Welcome to our class Henry."

    t "Hey Henry, Welcome!"

    h "Thank you! Eventhough the first day was kinda rough, I still think we will have fun"
    
    b "Yes, that is true. We both will have a lot of fun!"

    l "Can't you leave him alone."

    b "Shut up! You are lucky you're a girl."

    j "Heklo Hrenyd., sye yta topmrowe :)"
    
    "*You'are talking to yourself*"

    y "Oh man.. He just doesnt stop. Not even at home."

    "You fall asleep..."
    "Zzzzzz"

    "Day 2"
    scene bg outside
    play music 'ruins.mp3'
    show henry happy
    y "Hi Henry, wanna walk to class togehther?"

    h "T-Thank's but i need to v-visit the restroom first. W-Wanna come with me?"
    
    # Menu zum kopieren für Ali :-)

    #Hier fängt choice 4 an
    menu:

        "Yeah, sure!":
            jump choice4_yes

        "No, thanks I dont want to be late *smiling*":
            jump choice4_no
    
    label choice4_yes:
        scene bg bathroom
        #play music 'wc.mp3'
        show billy angry
        b "Hello new boy. Good to see you, i thought you wouldn't come to school today."
        

        menu:
            "Cant you take a break. Leave him alone":
                jump choice5_def

            "*Do nothing*": 
                jump choice5_done
        
        label choice5_def:
            b "Dont worry when I am finished here, you gonna be the next one"
            hide billy
            show rob happy:
                xalign 0.3
                yalign 1.0
            show jake happy:
                xalign 0.6
                yalign 1.0
            r "You have seen enough. Leave!"
            jump choice5_done

            label choice5_done:
                scene bg classroom
                "Enter classroom"
                show tom happy
                t "Have you seen Henry? He is late for class."
                y "Yes, I have seen him and he is in huge trouble."
                t "What you mean 'huge trouble'?"
                show tom sad
                y "Billy found him, I tried to help but the twins stopped me..."
                t "Look man. I know you are trying your best to help him but you need to watch out for your health as well"
                t "They will also target you when you go try to be annoying"
                t "There he is psssh"
                "*Bell rings*"
                play sound 'bell.mp3'
                "Billy, Rob and Jake join the class"
                hide tom
                show teach happy
                teach "Everybody sit down! Leslie collect the homework of everyone"
                hide teach
                show leslie happy
                l "Yes, mam!"
                hide leslie
                t "<Hey... where he is Henry. Didn't you say you saw him?>"
                teach "Who is talking? Is it you Jake? You wanna be suspended again?"
                j "No, please. It wasn't me."
                y "Yes, I did see him. Billy must have done something very bad"

            
            #hier weiter wegen defenden
            jump choice4_done

        

    label choice4_no:
        h "Alrighty see ya in class"
        y "yo!"
        hide henry
        scene bg classroom
        show tom happy
        t "Have you seen Henry? He is late today"
        y "I have seen him. He just went to the restroom"
        t "Oh, that not good. I saw Billy going there before class. Hopefully he didn't see him."
        "*Billy, Jake and Rob join the classroom*"
        "*Bell rings*"
        play sound 'bell.mp3'
        teach "Everybody sit down!"
        jump choice4_done

    label choice4_done:
        "*bell rings everybody is leaving*"
        play sound 'bell.mp3'
        "You are walking home"
        scene bg bedroom
        "*Phone is ringing*"
        play sound 'ring.mp3'
        b "*send a picture*"
        "Whole classgroup is laughing"
        j "bhbhbhbhbh"
        r "jnjmnknmkk"

        y "<No, this cant be true. Isn't that Henry???>"
        l "Delete this ASAP! This is not funny. This is way too much"
        h "*leaves chat"
        b "haha seems like someone didn't like it"
        "On the picture you see Henry's head deep in a toillete while Billy is laughing"
                
        y "I should have done something! Why am I like this"
        y "... but I can't do anything myself against 3"
        y "Henry, I'm so sorry. You don't deserve any of this..."

        scene bg outside
        show tom sad
        t "You have probably seen the photo..."
        y "yes."
        t "This is way too much even for Billy"
        y "..."
        t "Where is Henry? Maybe he is already in the classroom"
        y "Probably not..."

        scene bg classroom
        "*bells rings*"
        play sound 'bell.mp3'
        show teach happy
        teach "I have bad news... Henry left the school. He didn't like it and told me something about bullying idk. Leslie do your work"
        j "hahaha that's a new record Billy"
        r "You made him leave the school after 2 days!"
        





    #Hier endet choice 4
    # This ends the game.




    return
