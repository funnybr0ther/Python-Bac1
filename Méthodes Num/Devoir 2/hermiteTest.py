# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 2
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#


from matplotlib import pyplot as plt
from numpy import *
from hermite import hermiteeee

#
# -1- Interpolation d'un cercle :-)
#     avec les points et les dérivées exactes !
#

n = 4;
T = arange(0,3*pi/2,3*pi/(2*(n+1)))
T = append(T,[2*pi])

t = linspace(T[0],T[-1],1000)
X  =  cos(T); Y  =  sin(T);
dX = -sin(T); dY =  cos(T);

fig = plt.figure()
plt.plot(X,Y,'.r',markersize=10)
plt.plot(cos(t),sin(t),'--r')
plt.plot(hermite(t,T,X,dX),hermite(t,T,Y,dY),'-b')
plt.axis("equal"); plt.axis("off")
plt.show()
