def monster ():
    print ("as you ride through the lake, you notice the lake getting deeper and deeper before suddenly,a green levithan jumpes out of the water, it jaw unhinged")
    print ("you can either Jump or Stay in the boat, which would you like to do?")
    x = input()
    if x == "Jump":
        print ("you jump into the water as the levithan swallows your boat whole ")
        print ("your body is smacked into the walls of the lake by said beast, as you feel your spine actually crack")
        print ("your body is swung around by the water as the levithan dives and swims at you with unholy speed")
        print ("do you, dodge to the Right? or to the Left?")
        if x == "Right":
            print ("you dodge to the right in the water before stabbing it in the eye with your sword, and dragging said blade across it's body as it moved with unholy speed")
            print ("the levithan roars in pain before attempting to smack your body into the wall with it's fin, which happens, knocking the air out of your body as you feel your lungs get filled with water")
            print ("Do you Stay in the water? or Swim up?")
            if x == "Swim":
                print ("you swim up instantly, wanting to breath oxygen, and as you reach the top, the levithan swims after you and opens his mouth, swallowing you whole")
                from island import alone
                alone()
            if x == "Stay":
                print ("you decide to stay but the water is too much, you slowly drown, before getting bitten in half by the beast")
                print ("you died")
                exit()
        if x == "Left":
            print ("you dodge to the left, fear filling your body as you swing your sword at it's eyes, instead it smacks you into the wall, you feel light escaping your body")
            print ("you pass out")
            from cavecar import caveA
            caveA()
    if x == "stay":
        print ("you stay int the boat, yet it simply swallows you whole")
        from island import alone