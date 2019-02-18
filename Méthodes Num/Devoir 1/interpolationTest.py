# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 1
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#

from matplotlib import pyplot as plt
from numpy import *
from solveRatio import interpolation

#
# -1- Test de la fonction interpolation
#     On considère un jeu des 3 fonctions u(x)
#

n = 4; m = 100
x = (2*pi/(m))*arange(0,m+1)
X = (2*pi/(2*n+1))*arange(0,2*n+1)

functions = [lambda x : x*(x-2*pi)*exp(-x),
             lambda x : sin(x)+sin(5*x),
             lambda x : sign(x-2),
             lambda x : sin(x/7)*x,
             lambda x : sin(x**2 // 4*x)]

for u in functions:
  plt.figure()
  plt.plot(x,u(x),'-b',label='Fonction u')
  U = u(X)
  uh = polyval(polyfit(X,U,len(X)-1),x)
  plt.plot(x,uh,'-g',label='Interpolation polynomiale')
  uh = interpolation(X,U,x)
  plt.plot(x,uh,'-r',label='Interpolation trigonométrique')
  plt.plot(X,U,'ob')
  plt.xlim((-0.2,2*pi+0.2)); plt.ylim((-3,3))
  plt.title('Interpolation trigonométrique : 2n+1 = %d ' % len(X))
  plt.legend(loc='upper right')

plt.show()
