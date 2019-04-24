# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 6
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 

from matplotlib import pyplot as plt
from numpy import *

from doublePrime import doublePrime


#
# -1- Calcul de la derivee seconde de sin(1)
#     C'est facile : c'est -sin(1) :-)
#

x   = 1.0
u   = sin(x)
ddu = -u
  
#    
# -2- Quelques exemples de formules de differences finies
#

trials = [[-1, 0, 1],
          [-3,-2,-1, 0],
          [-2,-1, 0, 1, 2],
          [-4,-3,-2, 0, 1, 2]]

for iTrial in trials:
  alpha = array(iTrial)
  print("\n")
  print(" === Differences with : ",alpha)
    
#
# -2.1- Calcul des coefficients
#       Calcul de l'ordre de precision et du denominateur de l'erreur
    
  beta,gamma, order = doublePrime(alpha)

#    
# -2.2- Application de la formule avec h = 0.1
#       Comparaison erreur analytique et erreur estimee

  h = 0.1
  X = x + alpha*h
  U = sin(X)
  dduh = (U @ beta) / h**2
  eh = abs(h**order / gamma)
    
  print("  == dduh : %14.7e  (h = %5.0e)" % (dduh,h))
  print("  == order of the method : %12d" % order)
  print("  == denominator of the error :  %6.0f" % gamma)
  print("  == estimated error :   %14.7e" % eh)
  print("  == exact error :       %14.7e" % abs(dduh-ddu) )    
#
# -2.3- Joli plot
#

xplot = linspace(0,pi/2,100);
uplot = sin(xplot);
dduplot = -uplot
    
plt.figure("Differences with " + str(alpha))
plt.plot(xplot,uplot,'-r')
plt.plot(xplot,dduplot,'-b')
plt.plot([x,x],[u,ddu],'-k')
plt.plot(X,U,'or')
plt.plot(x,dduh,'ob')
plt.axis('equal')
plt.axis('off')
plt.show()


