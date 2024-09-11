num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxième nombre: "))

produit = num1 * num2

if produit < 1000:
    print("Le produit de", num1, "et", num2, "est:", produit)
else:
    print("Le produit de", num1, "et", num2, "est trop grand.")
    somme=num1 +num2
    print("La somme de", num1, "et", num2, "est:", somme)