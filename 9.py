num = int(input("entrer le nombre: "))

def Palindrome(num):
    s = str(num)
    return s == s[::-1]

if Palindrome(num):
    print(str(num) + " est un palindrome")
else:
    print(str(num) + " n'est pas un  palindrome")