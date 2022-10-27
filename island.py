def alone ():
    print ("you end up sitting withing the stomach of the beast, unable to escape it, it's acid slowly rising out")
    print ("you can only do so much, what will it be then? will you Climb up it's throat? or Slash at the fleshy walls surronding you?")
    x = input()
    if x == "Climb":
        print ("you stab your sword into part of the flesh and begin to climb the throat of the beast, as you climb further and further, you reach it's teeth ")
        print ("you can either Slash at the teeth or Sit by the Teeth")
        if x == "Slash":
            print ("you slash at the teeth nonstop, and suddenly, the beast opens his mouth, as so much water floods that it knocks you all the way back to the acid, burning you alive")
            print ("you died")
            exit()
        if x == "Sit":
            print ("you slowly sit to catch your breath, as you sit patiently, the boat it swalloed begins melting")
            print ("that causes it to vomit you up suddenly, as you get flung, you end up on a beach")
            print ("you stand up slowly and look around... gulping")
            from beach import island
            island()
    if x == "Slash":
        print ("you begin violently slashing everywhere")
        print ("that causes it stomach to become upset as it blechs you, vomitting you into the middle of the ocean")
        print ("you swim up and see a beach, do you Swim to it, or Catch your breath?")
        if x == "Swim":
            from beach import island
            island()
        if x == "Catch your breath":
            print ("before you can even do anything, the levithan smacks you with it's tail, blowing you into the atmosphere")
            print ("you have become a constellation ")
            exit ()