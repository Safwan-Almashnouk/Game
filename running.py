def lyra():
    print ("you ride for what feels like hours upon hours, panicking as you reach the kingdom, the sight steals away your breath.")
    print ("the kingdom you wished to reach and live in, it was destroyed, all of it flooded")
    print ("you smashed the gate open, before it happened, a gush of red liquid escaped through, hitting you and rolling you into a tree")
    print ("out of the liquid, she walked out, a woman with incredibly beauitful hair, and a pair of violet eyes, the princess of the stars, Lyra")
    print ("you are shocked by how beautfiul she is, tho then you see behind her, a man standing with his left arm on her shoulder... he had horns")
    print ("do you wish to Fight or Run?")
    x = input()
    if x == "Fight":
        from boss import fight
        fight()
    if x == "escape":
        from run import ohNo
        ohNo()
    