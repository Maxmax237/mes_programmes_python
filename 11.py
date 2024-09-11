n=int(input("saisir la avaleur de n"))
inverse =0
while n!=0:
    inverse = (inverse*10)+(n%10)
    n=n//10
    print("linverse",inverse)
