print ("You are a young knight, wishing one day to reach and become a member of the five stars, the strongest guardians of your kingdom, and possibly even meet the princess, the beautfiul black haired princess. ")
print("you wake up with a bad feeling today, nonetheless its time to go to the kindgom for your exam, if you do well, you can rise from novice to a higher ranked knight.")
print ("you had spent a long mission outside the kingdom, on a farm, after having breakfast, you deicede to go.")
print ("how would you like to go?")
print ("A is via a passing Carriage")
print ("B is via your white steed")
print ("C is via a long long walk")
print ("D is via the boat in the lake ")

A = "A"
B = "B"
C = "C"
D = "D"
X = input()

if X == A:
    print ("you get onto the side of the road and put your arm up ")
    from carr import carriages
    carriages()

if X == B:
    print ("you get onto your white steed, the steed seems excited, as you set off on your journey")

if X == C:
    print ("you deicede to walk, a rather stupid idea, but hey, excericese right?")

if X == D:
    print ("you get on the boat and let the stream of the river take you")
