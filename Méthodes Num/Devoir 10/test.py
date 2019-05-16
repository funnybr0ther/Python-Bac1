# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 10
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#
 
from numpy import *
from timeit import default_timer as timer
from poisson import poissonSolve
 
 
n = 20
tic = timer()
U = poissonSolve(n) 
print("      Elapsed time : %f seconds" % (timer() - tic))
print(" ==== Maximum value of U : %10.8f " % amax(U))
print(" ==== Minimum value of U : %10.8f " % amin(U))
 
 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
myColorMap = matplotlib.cm.jet
 
 
X = linspace(-1,1,2*n+1); U = abs(U)
plt.figure("Python as Matlab clone...")
plt.contourf(X,X,U,10,cmap=myColorMap)
plt.contour(X,X,U,10,colors='k',linewidths=1)
plt.hlines(X,X.min(),X.max(),color='white',linewidths=0.5)
plt.vlines(X,X.min(),X.max(),color='white',linewidths=0.5)
plt.axis("off"); plt.axis("equal")
plt.show()
