# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 7
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#

from numpy import *
from matplotlib import pyplot as plt
from lorenz import lorenz

plt.figure("Lorenz Equations")
Xstart = 0; Xend = 100;
Ustart = [0,1,0]
n = 10000;

X,U = lorenz(Xstart,Xend,Ustart,n)
plt.plot(U[:,0],U[:,2],'-r',linewidth=0.5)
plt.show()
