def quest_start():
    print ("Lodran, the village you just entered, you relize there is quite a lot of giant rat, and in seconds, a giant rat, one with a mohawk approaches you")
    print ("do you Run or Fight?")
    x = input ()
    if x == "Run":
        from mauled import ouch 
        ouch()
    if x == "Fight":
        from ratking import skinned
        skinned ()