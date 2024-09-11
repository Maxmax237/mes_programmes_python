n=int(input("saisir la avaleur de n"))
p=int(input("saisir la avaleur de p"))
# Calculer les deux expressions
puissance = p ** n
produit = 1
for i in range(n):
    produit *= p

# Comparaison
est_egal = puissance == produit
print(f"p^{n} = {puissance}")
print(f"p * p * p* p(n fois) = {produit}")
print(f"L'égalité est vraie : {est_egal}")