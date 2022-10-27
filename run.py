def ohNo():
    print ("you turn around and begin running")
    print ("that's when the princess, in her soft voice spoke 'your kind is unwelcome here'")
    print ("and with that, the demon simply swings his forearm and sends you flying through multiple trees")
    print ("you are laying on the ground, blood just dripping from your nose, and then, it comes to you... Will you try to Escape? or Stay?")
    x = input()
    if x == "Escape":
        from crawl import despair
        despair()
    if x == "Stay":
        from despair import crushed
        crushed()