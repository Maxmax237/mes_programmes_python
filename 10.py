# Liste d'exemple
premiere_liste = [10, 20, 25, 30, 35]
seconde_liste = [40, 45, 60, 75, 90]

# Extraire les nombres impairs de la première liste
nombres_impairs_premiere = [x for x in premiere_liste if x % 2 != 0]

# Extraire les nombres pairs de la seconde liste
nombres_pairs_seconde = [y for y in seconde_liste if y % 2 == 0]

# Créer une nouvelle liste avec les nombres pairs de la première liste et de la seconde
nouvelles_liste = nombres_impairs_premiere + nombres_pairs_seconde

print("Nombres impairs de la première liste :", nombres_impairs_premiere)
print("Nombres pairs de la seconde liste :", nombres_pairs_seconde)
print("Nouvelle liste :", nouvelles_liste)