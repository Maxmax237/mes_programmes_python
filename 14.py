n = int(input("saisir le nombre de lignes : "))

for j in range(n , 0 , -1):
    for i in range(j , 0 , -1):
        print("*" , end = "")
    print('\r')