def mistake():
    print ("you wait with the scared father, before suddenly, you see a sillhoute, before a woman came out of the shadows, a ghostly woman with silver hair")
    print ("the woman lifts her dettached head and lets out a blood boiling scream, and it causes you to feel an unholy amount of frenzy for blood, but your amulet, a gift from your mother protects you from being mind controlled")
    print ("the father next to you however is not as lucky, screaming as he pulled out a knife, and in the blink of an eye, he turns around to attack you, only for his own daughter to suddenly slit his throat")
    print ("the daughter looks at you, blood all over her as she swings the knife at you ")
    print ("do you, A, attack? or do you B defend?")
    X = input()
    if X == "A":
        print ("you get in your stance with impressive speed, gripping your sword you swing it down at extreme speed, the sword breaks through her guard and slices a massive wound across her body, killing her instantly.")
        print ("her blood splatters all over you, yet her body forces itself to drive the blade into your leg, earning a scream of pain to escape your lips as you pull away from her ")
        print ("you can either Escape or Fight")
        if X == "Escape":
            from fall import fall_func
            fall_func()
        if X == "Fight":
            print ("you decide to slash nonstop, roaring, yet the ghost go through your attacks and their blades get drived through your body, and you are torn apart")
            print ("death")
            exit()

    if X == "B":
        print ("you quickly get ready to defend against her attack, yet thanks to her height, she easily slips past you and stabs your thigh, before driving her blade down and cutting open your thigh.")
        from attack import escape
        escape ()