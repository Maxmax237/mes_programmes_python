def calcul_impot(revenu):
    impot = 0

    if revenu <= 10000:
        impot = revenu * 0
    elif revenu <= 20000:
        impot = 10000 * 0 + (revenu - 10000) * 0.10
    else:
        impot = 10000 * 0 + 10000 * 0.10 + (revenu - 20000) * 0.20

    return impot

# Exemple d'utilisation
revenu = 45000
impot_a_payer = calcul_impot(revenu)
print(f"L'impôt sur le revenu pour un revenu de ${revenu} est de ${impot_a_payer:.2f}.")