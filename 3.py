mot=input ('enter le mot\n')
indice=[mot[i]for i in range (len(mot))if i%2==0]
print("les caracteres aux indices paires:",",".join(indice))