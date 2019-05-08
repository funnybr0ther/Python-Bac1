# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 9
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#

from numpy import *
import matplotlib 
import matplotlib.pyplot as plt 
from timeit import default_timer as timer

from diffusion import diffusion,diffusionSmart


matplotlib.rcParams['toolbar'] = 'None'
myColorMap = matplotlib.cm.jet

#
# -1- Parametres physiques et numériques de la simulation
#     "factor" permet de raffiner dt et dx 
#

factor = 10
n = 4*factor; nMid = int((n)//2)
nt = 2*factor*factor
Trange = arange(0,1.1,0.1)
X,Y = meshgrid(linspace(-1,1,n+1),linspace(-1,1,n+1))

beta = 0.25
#beta = 0.2525    # Pour voir les instabilités :-)

#
# -2- Evolution temporelle
#

plt.figure("Thermal diffusion : beta = %6.4f" % beta)
T = zeros((n+1,n+1)); T[0,:] = 1
for i in range(4):
  plt.subplot(2,2,i+1)
  T = diffusion(T,beta,nt)
  plt.contourf(X,Y,T,Trange,cmap=myColorMap)
  plt.contour(X,Y,T,Trange,colors='k',linewidths=1)
  plt.axis("off"); plt.axis("equal")
  plt.title("Iteration = %d " % (nt*(i+1)))
  

#
# -Comparaison de l'implémentation de base
#  et du calcul restreint à une demi-domaine en tirant profit
#  de la symétrie :-)
#

plt.figure("Comparing both implementations !")

nt = 4*nt
T = zeros((n+1,n+1)); T[0,:] = 1
tic = timer(); T = diffusion(T,beta,nt)
print(' === Basic version \n   Elapsed time is %f seconds.' % (timer() - tic))
print('   T(L/2,L/2) = %10.6f [K] after %d steps ' % (T[nMid,nMid],nt))
Tbasic = T[nMid,nMid]

plt.subplot(1,2,1)
plt.contourf(X,Y,T,Trange,cmap=myColorMap)
plt.contour(X,Y,T,Trange,colors='k',linewidths=1)
plt.axis("off"); plt.axis("equal")
plt.title("Basic version...")


X,Y = meshgrid(linspace(0,1,nMid+1),linspace(-1,1,n+1))
T = zeros((n+1,nMid+1)); T[0,:] = 1
tic = timer(); T = diffusionSmart(T,beta,nt)
print(' === Smart version \n   Elapsed time is %f seconds.' % (timer() - tic))
print('   T(L/2,L/2) = %10.6f [K] after %d steps ' % (T[nMid,0],nt))
print('   Differences between both implementations : %14.7e ' % abs(Tbasic-T[nMid,0]))

plt.subplot(1,2,2)
plt.contourf(X,Y,T,Trange,cmap=myColorMap)
plt.contour(X,Y,T,Trange,colors='k',linewidths=1)
plt.contourf(-X,Y,T,Trange,cmap=myColorMap)
plt.contour(-X,Y,T,Trange,colors='k',linewidths=1)
plt.axis("off"); plt.axis("equal")
plt.title("Smart version :-)")

plt.show()


