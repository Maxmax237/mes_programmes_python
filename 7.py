def compter_emma(texte):
    # Initialiser le compteur à 0
    compte = 0

    # Convertir le texte en minuscules pour une recherche insensible à la casse
    texte_minuscules = texte.lower()

    # Parcourir le texte caractère par caractère
    index = 0
    while index < len(texte_minuscules):
        # Rechercher l'occurrence suivante de "emma"
        index_emma = texte_minuscules.find("emma", index)

        # Si "emma" n'est pas trouvé, sortir de la boucle
        if index_emma == -1:
            break

        # Vérifier si la sous-chaîne trouvée correspond bien à "Emma" et pas à "Emmaline" ou autre
        if texte[index_emma:index_emma+4] == "Emma":
            # Incrémenter le compteur
            compte += 1

        # Passer à la prochaine position de recherche
        index = index_emma + 1

    return compte

# Exemple d'utilisation
texte= "Emma a eu son prenom de sa grand-mere qui se prenommait Emma",
"elle aussi a son elle a donné le prenom Emma à sa fille"
"Maintenant le prenom Emma est dans toutes les bouches Emma par ici Emma par là"
nb_emma = compter_emma(texte)
print(f"Le mot 'Emma' apparaît {nb_emma} fois dans le texte.")