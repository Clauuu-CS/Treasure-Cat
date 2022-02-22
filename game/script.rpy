
define c = Character("Cat", color="bc92e1")
define m = Character("Me", color="a461de")

## $ counter = int(1)
$ right = True

label start:
    $ wrong = False
    scene bg black

    c "Wake up...Wake up..."

    scene bg eye with fade
    scene bg black with fade

    c "Hey you!"

    scene bg eye with fade
    scene bg black with fade

    c "Yes you! Wake up!"
    c "..."
    scene bg white with fade
    show cat normal  with fade

    c "There you are, it wasn't that hard wasn't it?"
    c "Hi, my name is Shadow."
    c "Well, now that you are awake it is the perfect moment to tell you  that I know where your precious treasure is."
    m "My what?"
    c "Your treasure: the most valuable asset that you own. "
    show cat question
    c "You don't remeber?"
    m "..."
    show cat happy
    c "*smirk"
    m "Well, if it is mine, could you tell me where it is?"
    show cat question
    c "Mmmmm..."
    show cat normal
    c "No"
    m "No? Why not? It is  indeed mine, isn't it?"
    c "Yes, but you shouldn't have lost it in the first place."
    m "But you just told me it was a great time to tell me."
    c "..."
    show cat annoyed
    c "Oh, don't look at me like that!"
    c "Look, since I am terribly bored today I'll allow you to play a game with me."
    show cat normal
    c "If you answer my questions correctly, I'll lead you onto your treasure. But if you don't then you will never know where it is hidden."
    c "So...what do you say?"

    menu:
        "No, thank you.":
            jump bad_ending
        "Ok.":
            jump continuation_0

label continuation_0:
    show cat happy
    c "Great! Now follow me."
    hide cat normal with fade
    scene bg land with fade
    pause 2

label continuation_1:
    $ wrong = False
    show cat normal
    c "Ok, so first question:"
    c "How many toes do you think I have?"
    menu:
        "20":
            $ wrong = True
        "5":
            $ wrong = True
        "69":
            $ wrong = True
        "18":
            ## right answer
            $ right = True
        "None":
            $ wrong = True
    c "Ok, interesting answer... Next question!"
    m "Wait, aren't you going to tell me whether I got it right?"
    show cat happy
    c "No."
    c "Second question!"
    show cat normal 
    c "What's my name? ( I told  you before btw ) "
    menu:
        "Leo":
            $ wrong = True
        "Bob":
            $ wrong = True
        "Parsa":
            $ wrong = True
        "Sera":
            $ wrong = True
        "Shadow":
            ## right answer
            $ right = True
    c "Ok. Next question!"
    show cat hid
    c "Where am I hidden?"
    menu:
        "Space":
            $ wrong = True
        "Nowhere":
            $ wrong = True
        "Behind the bush":
            $ right = True
        "Behind the tree":
            $ wrong = True
        "Underground":
            ## right answer
            $ wrong = True

    if wrong == True:
        jump wrong_answer

    if wrong == False:
        jump good_answer

label wrong_answer:
    show cat normal
    c "Ok... It seems you have made a mistake at some point."
    c "I'm afraid I can't give you your tresure back."
    c "I'm feeling generous today, so would you like to try again?"
    
    menu:
        "No, thank you.":
            jump bad_ending
        "Ok.":
            jump continuation_1

label good_answer:
    show cat happy
    c "YEY! You have answered all my questions right!"
    c "I'm happy to say that you have gained the right to recieve your tresure."
    c "Here you have..."
    scene bg eye with fade
    scene bg black with fade
    scene bg eye with fade
    scene bg black with fade
    "You suddenly wake up in your bed. It is a bright day in the morning, and your alarm clock has just started rigning."
    "You look at the end of the bed and see your cat Shadow snuggled up and sleeping."
    m "Well...that was a strage dream..."
    "THE END"
    return 

label bad_ending:
    show cat normal
    c "Ok, then. You do you."
    hide cat
    scene bg eye with fade
    scene bg black with fade
    scene bg eye with fade
    scene bg room_night with fade
    "You have played \"counter\"times. Do you want to keep playing?"
    menu:
        "Yes":
            ## $ counter = counter + 1
            scene bg eye_room_night with fade
            scene bg black with fade
            m "I feel so sleepy..."
            scene bg eye_room_night with fade
            scene bg black with fade
            jump start

        "No":
            scene bg black with fade
            pause 3
            return
