
#1. Création de fonction mathématique simple en Python (12 points) :
#a) Implémenter la fonction polynomiale ci-dessous :

#f(x)=x3-1,5x2-6x+5


print('hello')
print('Donnez la valeur de X')
x = float(input('x='))
def calcul_polynome(x):
      return x**3-1.5*x**2-6*x+5
print(calcul_polynome(x));

#b) Implémenter la fonction factorielle (Approche récursive ou classique) :
#Soit n un entier naturel, on définit la fonction factorielle comme :

def f_facto(x):
  x = int(input('indiquez la valeur : X = '))
  if x == 0:
    return 1
  else :
    f = 1
    for n in range(2,x+1):
      f = f*n
    return f;
f_facto(x)

#c) Implémenter la suite de Fibonnaci

n = int(input ("Entrer la valeur MAX : "))
I0 = 0
I1 = 1
for n in range(2,n):
  In = I0 + I1
  print(In)
  I0 = I1
  I1 = In
