def compare_premiers_derniers(tableau):
    if len(tableau) > 0:
        premier_nombre = tableau[0]
        dernier_nombre = tableau[-1]
        print (f"Le tableau est : {tableau}")
        print(f"Le premier nombre est : {premier_nombre}")
        print(f"Le dernier nombre est : {dernier_nombre}")
        if premier_nombre == dernier_nombre:
            print("True")
        else:
            print("False")
premier_nombre  = [10, 20, 30, 40, 10]
print("le resultat",compare_premiers_derniers (premier_nombre))

dernier_nombre = [75, 65, 35, 75, 30]
print("resultat", compare_premiers_derniers(dernier_nombre))
 