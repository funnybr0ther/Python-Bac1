# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 8
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
#
  
from numpy import *
from scipy.linalg import norm
from ladders import laddersSolve,laddersIterate
  
#
# -1- Calcul de l'écart entre les deux murs :-)
#
  
geometry = [3,4,1]
print(" ========= my Newton-Raphson scheme with your proposed step :-)")
  
x = array([1.0,1.5]); tol = 10e-12; nmax = 50
n = 0; delta = tol+1
while (norm(delta) > tol and n < nmax):
  xold = x
  x = laddersIterate(geometry,xold)
  delta = array(x)-array(xold); n = n+1
  print(" Estimated error %9.2e at iteration %d : " % (norm(delta),n),x)
print(" Computed distance is : %13.6f " % sum(x))
  
  
print(" ========= your full computation :-)")
sol = laddersSolve(geometry,1e-14,50)
print(" Computed distance is : %13.6f " % sum(sol))
  
a = geometry[0]
b = geometry[1]
c = geometry[2]
ab = max(a,b)
  
#
# -2- Et un joli dessin
#
  
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
plt.rcParams['figure.facecolor'] = 'silver'
  
plt.figure("Ladders geometry")
x = sol[0]; y = sol[1]; d = x + y
hx = sqrt(b*b - d*d); hy = sqrt(a*a - d*d)
plt.plot([-x,y],[hx,0],'-r')
plt.plot([-x,y],[0,hy],'-b')
plt.plot([-x,-x,y,y],[ab,0,0,ab],'k')
plt.axis('equal')
ax = plt.gca()
ax.yaxis.grid(color='gray',linestyle='dashed')
ax.xaxis.grid(color='gray',linestyle='dashed')
plt.xticks(arange(-ab,ab+1,1))
plt.yticks(arange(0,ab+1,1))
plt.show()