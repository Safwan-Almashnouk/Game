def skinned ():
    print ("you pull your sword out instantly, relying on your instinct and skills you have a quick decison ")
    print ("do you, use a Speed buff or a Attack buff?")
    x = input()
    if x == "Speed":
        print ("you yell 'SPEED INCREASE' before you flash past the rat, slicing through his neck and causing blood to shoot everywhere, and espically all over you")
    if x == "Attack":
        print ("you yell 'ATTACK BUFF' before dashing forward and using the blunt of your weapon, thus the side of the sword to smash it through his skull, causing blood to burst all over you")

    print ("after the ordeal, the villagers all slowly walk out of their homes. The rats all escpaing through the holes in the ground ")
    print ("the village chief thanks you and asks if you wish to stay over, what is your response? Yes? or No?")
    if x == "Yes":
        from lore import fall
        fall ()