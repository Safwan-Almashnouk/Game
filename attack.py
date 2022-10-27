
def escape():
    print ("you have a mild injury in your leg, do you wish to Escape? or Fight?")
    X = input()
    if X == "Escape":
        print ("you swallow your pride, fighting through the pain, you run out of the forest full speed, not looking back as you force your bleeding leg to run")
        from fall import fall_func
        fall_func("Attack")
    if X == "Fight":
        print ("you refuse to escape, gripping your sword you dash at the ghostly lady and slash, your attack tho phase through their bodies. that is when you feel a sharp pain as multiple ghosts stab their blade like arms into you, tearing you apart limb from limb, your screams soon are as quiet as the night")
        print ("you have died")
        exit()