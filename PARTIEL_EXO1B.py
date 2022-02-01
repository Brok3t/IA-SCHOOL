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
