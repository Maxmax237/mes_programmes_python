def diviser_tableau_par_5(div):
    resultat = []
    for element in div:
        resultat.append(element / 5)
    return resultat
div = [10, 20, 33, 46, 55]
nouveau_tableau = diviser_tableau_par_5(div)
print(nouveau_tableau)