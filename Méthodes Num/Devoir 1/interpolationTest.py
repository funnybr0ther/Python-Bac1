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
# -1- Test de la fonction interpolation13119
#     On considère un jeu des 3 fonctions u(x)
#

n = 9; m = 100
x = (5*pi/(m))*arange(0,m+1)
X = (2*pi/(2*n+1))*arange(0,2*n+1)
print(X)
functions = [lambda x : x*(x-2*pi)*exp(-x),
             lambda x : sin(x)+sin(5*x),
             lambda x : sign(x-2),
             lambda x : sin(x/7)*x,
             lambda x : sin(x**2) // 4*x]
X = array([0,2,4,7.4,10,12,14,15])
U = array([5,4,2,1,0.4,0.2,0.135,0.09])
uh = polyval(polyfit(X,U,len(X)-1),x)
plt.plot(x,uh,'-g',label='Interpolation polynomiale')
plt.plot(X,U,'ob',label ='Valeurs mesurées')
plt.xlabel("distance (cm)")
plt.ylabel("Tension L_2 (V)")
plt.legend(loc='upper right')

plt.show()
