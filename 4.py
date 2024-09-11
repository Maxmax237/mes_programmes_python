mot=input("Entrer un mot\n")
indice=[mot[i]for i in range(len(mot))if i-1==0]
print("les lettres sont supprimés".join(indice))