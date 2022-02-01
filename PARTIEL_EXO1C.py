
#1. Création de fonction mathématique simple en Python (12 points) :
#a) Implémenter la fonction polynomiale ci-dessous :

#f(x)=x3-1,5x2-6x+5


print('hello')
print('Donnez la valeur de X')
x = float(input('x='))
def calcul_polynome(x):
      return x**3-1.5*x**2-6*x+5
print(calcul_polynome(x));
