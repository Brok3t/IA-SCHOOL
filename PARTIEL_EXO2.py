# 2. Création de fonction comportant des modules de gestions des  exceptions (5 points) :

def polynome(x):
    a = 1
    while a == 1 :
        try :
            x = float(input("x = "))
            if x < 0 :
                print("La valeur ne doit pas être négative")
                break
            if x < 0.00001 :
                print("La valeur rentrée est trop petite")
                break
            if x > 999999 :
                print("La valeur entrée est trop grande")
                break

            resultat = (x*3)-(1.5*x*2)-(6*x)+5
            return resultat
            a = 2
        except :
            a = 2
            print('Une valeurs numériques est attendue ici')
            break

    print(polynome(x))
