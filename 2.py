print("affichage d'un nombre actuel de son precedent et  sum in a range")
precedent = 0
for i in range(0, 10):
    somme= precedent + i
    print("nombre actuel", i, "precedent ", precedent, " Sum: ", somme)
    precedent = i