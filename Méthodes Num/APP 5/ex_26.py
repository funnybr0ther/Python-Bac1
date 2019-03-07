from numpy import *
from matplotlib import pyplot as plt
from numpy.linalg import solve
ti = linspace(0,3,4)
Xi = array([0,1,0,0])
Yi = array([0,0,1,0])
matrix = array([pow(i,ti) for i in ti])
coeff_x = solve(matrix, Xi)
coeff_y = solve(matrix, Yi)
x = linspace(0,3,250)
ux = array([dot(coeff_x,array([1,t,pow(t,2),pow(t,3)])) for t in x])
uy = array([dot(coeff_y,array([1,t,pow(t,2),pow(t,3)])) for t in x])
"""
y = [0.5]
ul = array([dot(coeff_x,array([1,t,pow(t,2),pow(t,3)])) for t in y])
ud = array([dot(coeff_y,array([1,t,pow(t,2),pow(t,3)])) for t in y])
print(ul)
print(ud)
"""
plt.plot(ux,uy,"r")
def b(t,T,i,p):
  if p == 0:
    return (T[i] <= t)*(t < T[i+1])
    # =1 si les deux conditions sont vérifiées
  else:
    u  = 0.0 if T[i+p ]  == T[i]   else (t-T[i])/(T[i+p]- T[i]) * b(t,T,i,p-1)
    u += 0.0 if T[i+p+1] == T[i+1] else (T[i+p+1]-t)/(T[i+p+1]-T[i+1]) * b(t,T,i+1,p-1)
    # le if vérifie si le dénominateur n'est pas nul
    return u
p = 2
T = linspace(-2,5,dtype = int)
n = size(T)
tx = [0,1,2,3]
Bx = zeros((n-p,len(tx)))
for i in range(0,n-p):
    Bx[i,:] = b(tx,T,i,p)
ty = [0,0,1,0]
By = zeros((n-p,len(ty)))
for i in range(0,n-p):
    By[i,:] = b(ty,T,i,p)





plt.show()