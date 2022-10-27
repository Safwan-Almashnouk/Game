def fall():
    print("after you sit down and get cleaned from the dirty blood, just incase, you are given medicine")
    print ("after you tell the village chief about your mission, he says something that suprsies you")
    print ("'The kingdom? of the stars? have you not heard? it collapsed, a tradgedy struck the kingdom, a demon appeared and wiped it out, i suggest abandoning your mission if i am honest, you are lucky you were not there,' ")
    print ("out of shock, you feel your heart drop, yet if what he spoke is true.... should you go?")
    print ("you can either Run to the kingdom, or Stay, which would you like?")
    x = input ()
    if x == "Run":
        from running import lyra
        lyra()
    if x == "Stay":
        from ending1 import peace
        peace()

